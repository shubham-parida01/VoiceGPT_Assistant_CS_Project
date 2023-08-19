import openai

openai.api_key = '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'


def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user',
                   'content': prompt}]
    )
    return response["choices"][0]['message']['content']

print(chat_gpt('WHat are you ?'))


