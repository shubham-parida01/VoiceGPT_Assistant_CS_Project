import openai

openai.api_key = 'sk'


def chat_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user',
                   'content': prompt}]
    )
    return response["choices"][0]['message']['content']