import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are my personal assistant"}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


interface = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Personal Assistant")

interface.launch(share=True)
