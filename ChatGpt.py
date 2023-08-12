import openai

openai.api_key = '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'


def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user',
                   'content': prompt}]
    )
    return response["choices"][0]['message']['content']


