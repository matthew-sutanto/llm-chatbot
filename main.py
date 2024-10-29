from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

chat_model = ChatOllama(model="llama3.2:1b")

messages = [
    SystemMessage("You are a very angry person. You don't like being in a conversation and will always want to make the other person stop talking.")
]

while (True):
    inp = input("You: ")
    messages.append(HumanMessage(content=inp))
    response = chat_model.invoke(messages)
    print(f"Bot: {response.content}")
    messages.append(AIMessage(content=response.content))
    print("Messages", messages)