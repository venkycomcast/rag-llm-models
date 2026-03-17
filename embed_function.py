from ollama import embed, chat

embeddings = embed(model="custom_qwen", input=["Here is an example sentence", 'Here is a second one!']);

print(len(embeddings.embeddings[0]))
