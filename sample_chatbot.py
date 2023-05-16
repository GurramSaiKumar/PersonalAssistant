import openai

openai.api_key = "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"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Give me 3 ideas to make money using chat gpt"}
    ]
)
if response['object'] == 'chat.completion':
    print(response['choices'][0]['message']['content'])
else:
    print("no response")
