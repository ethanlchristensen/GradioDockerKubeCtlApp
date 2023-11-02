import os
import json
import time
import flask
import openai

from flask import (
    request, jsonify
)
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

SP = """You are an AI assitant that takes in a piece of text and tries to summarize it in 2-5 sentences."""

TP = """You are an AI assitant that takes in a piece of text and extracts topics from the text."""

def complete(system_prompt: str, user_prompt: str) -> str:
    start = time.time()
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        max_tokens=400
    )
    time_to_complete = time.time() - start
    return completion.choices[0].message.content, time_to_complete

@app.route('/', methods=['POST'])
def home():
    return "<h1>Hello from Azure Hackthon! :)</h1>"

@app.route('/api/v1/summarize', methods=['POST'])
def summarize():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = json.loads(request.data)
        if data.get('context'):
            summary, ttc = complete(
                system_prompt=SP,
                user_prompt=data.get('context')
            )

            return {
                "status": "success",
                "message": summary,
                "timeToComplete": ttc,
                "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
          return {
            "status": "error",
            "message": "Context to summarize must be provided."
        }  
    else:
        return {
            "status": "error",
            "message": "Unsupported content type."
        }
    
@app.route('/api/v1/topics', methods=['POST'])
def topcis():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        data = json.loads(request.data)
        if data.get('context'):
            if data.get('numberTopics'):
                topics, ttc = complete(
                    system_prompt=TP,
                    user_prompt=f"Generate {data.get('numberTopics')} topics, not numbered, seperated by a newline for the following text:\n{data.get('context')}\n\nTopics:\n"
                )

                return {
                    "status": "success",
                    "message": topics.split('\n'),
                    "timeToComplete": ttc,
                    "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            else:
                return {
                    "status": "error",
                    "message": "Number of topics must be provided."
                }
        else:
          return {
            "status": "error",
            "message": "Context to summarize must be provided."
        }  
    else:
        return {
            "status": "error",
            "message": "Unsupported content type."
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
