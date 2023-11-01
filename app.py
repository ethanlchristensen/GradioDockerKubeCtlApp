import gradio as gr
import openai

openai.api_key = ""

def complete(system_prompt: str, user_prompt: str) -> str:
    completion = openai.ChatCompletion.create(
        # model="gpt-3.5-turbo-16k",
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
    return completion.choices[0].message.content

# def extract_n_topics(text, question):
def extract_n_topics(question):
    return complete(
        # "You are given a piece of text from a user and are to extract the specificed number of topics or less from the text. Respond with just the list and nothing else.",
        # "You are given a piece of text from a user and a question. Respond with an answer to the question. If you don't know the answer, polietly decline.",
        "Answer the given question from the user. Act like a newbie programmer that write extra lines of code for no reason. Don't tell them your persona, just respond like an epic baws.",
        # f"Text: {text}\nQuestion: {question}\nAnswer: "
        f"Question: {question}\nAnswer: "
    )

with gr.Blocks() as demo:
    gr.Markdown("Input a Piece of Text, Adjust the slider to desired topics, and click 'Extract'!")
    with gr.Row():
        # query = gr.TextArea(placeholder="Enter text")
        question = gr.TextArea(placeholder="Enter Question")
    btn = gr.Button("Run")
    out = gr.Markdown()
    # btn = gr.Button("Extract Topics")
    btn.click(fn=extract_n_topics, inputs=[question], outputs=[out])

# demo.launch(
#     server_name="0.0.0.0",
#     server_port=7860
# )
demo.launch()