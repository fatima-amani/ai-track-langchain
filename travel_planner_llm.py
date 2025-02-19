from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral", temperature=0.1, max_tokens=500)

prompt = """ Act as a travel Planner and generate itinerary for a {num_of_days} day trip to {place}. List some popular places to visit and a list of popular restaurants."""
prompt_template = PromptTemplate(template=prompt, input_variables=["num_of_days", "place"])

while True: 
    place = input("User: The Place you want to visit: (or exit)  ")
    if place.lower() == "exit" or place.lower() == "quit":
        break
    num_of_days = input("User: Num of days: ")
    output = llm.invoke(prompt_template.format(num_of_days=num_of_days, place=place))
    # print(llm.invoke("Say hello"))
    print(f"Bot: {output}")