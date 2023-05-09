import openai
import pyperclip
import gpt_api

API = gpt_api.GPT_API()
openai.api_key = API
model_id = 'gpt-3.5-turbo'

def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    print('Total de tokens usados: {0}'.format(api_usage['total_tokens']))
    print(response['choices'][0].finish_reason)
    print(response['choices'][0].index)
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return response

conversation = []

def main():
    ask = input('Como posso ajudar?\n')
    conversation.append({'role': 'system', 'content': ask})

    conversa = ChatGPT_conversation(conversation)
    print('IA: {0}'.format(conversa['choices'][-1]['message']['content']))
    pyperclip.copy(conversa['choices'][-1]['message']['content'])

def continue_conversation():
    ask2 = input('Usuário: ')
    conversation.append({'role': 'user', 'content': ask2})
    conversa = ChatGPT_conversation(conversation)
    print('IA: {0}'.format(conversa['choices'][-1]['message']['content']))
    pyperclip.copy(conversa['choices'][-1]['message']['content'])

main()
while True:
    continue_conversation()