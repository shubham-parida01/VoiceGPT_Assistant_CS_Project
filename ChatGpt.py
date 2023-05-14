import openai

openai.api_key = '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'


def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user',
                   'content': prompt}]
    )
    return response["choices"][0]['message']['content']



