from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chat_history = [
    SystemMessage("You are a helpful assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.strip().lower() == "exit":
        print(chat_history)
        break
    result = model.invoke(chat_history) 
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)