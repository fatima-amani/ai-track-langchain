from langchain_ollama import OllamaLLM

llm = OllamaLLM(model='phi3', temperature=1, max_tokens=10)


while True:
    topic = input("User: Explain to me about: ")
    if topic.lower() == "exit" or topic.lower() == "quit":
        break
    output = llm.invoke(topic)
    print(f"Bot:{output}")