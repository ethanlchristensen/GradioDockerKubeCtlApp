import json
import requests
import gradio as gr

def call_api(text, option):
    print(option)
    option = option.lower() if option == 'Summarize' else 'topics'
    url = 'http://host.docker.internal:7860/api/v1/%s' % option

    print(url)

    payload = {
        "context": str(text)
    }

    headers = {
        'Content-Type':'application/json'
    }

    if option == 'topics':
        payload['numberTopics'] = 5

    payload = json.dumps(payload)

    response = requests.request('POST', url, headers=headers, data=payload)

    response = json.loads(response.content.decode('utf8'))
    if option == 'topics':
        return '\n'.join(response['message'])
    else:
        return response['message']


with gr.Blocks() as demo:
    gr.Markdown('Input a Piece of Text and select what you want to do. Then click "Run"!')
    with gr.Row():
        text = gr.TextArea(label="Input Text")
        option = gr.Dropdown(choices=['Summarize', 'Topic Extraction'])
    btn = gr.Button('Run')
    out = gr.TextArea(label="Output")
    # btn = gr.Button("Extract Topics")
    btn.click(fn=call_api, inputs=[text, option], outputs=[out])

if __name__ == "__main__":
    # demo.launch(
    #     server_name="0.0.0.0",
    #     server_port=7861
    # )
    demo.launch(server_port=7861)
