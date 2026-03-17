from ollama import embed, chat

response = chat(model='deepseek-r1:8b', messages=[
  {
    'role': 'user',
    'content': 'Why did the chicken cross the road?',
  },
])

print(response.message.content)