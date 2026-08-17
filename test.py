# from tools.tavily_tool import tavily_search
# from tools.flight_tool import search_flights
# from backend import run_travel_agent

# # res = tavily_search("what is the capital of Pakistan?")
# # print(res)

# # res = search_flights("Plan a 7 days Dubai trip from Pakistan")
# # print(res)


# user_input = input("Enter travel request: ")

# response = run_travel_agent(
#     user_input=user_input,
#     thread_id="test_user"
# )

# print("\nFINAL RESPONSE:\n")
# print(response["answer"])

import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq
llm = ChatGroq(
    model=os.getenv("GROQ_MODEL_NAME", "llama-3.3-70b-versatile"),
    api_key=GROQ_API_KEY
)

try:
    res = llm.invoke("What is the Capital of Pakistan?")
    print(res.content)
except Exception as e:
    print("ERROR CALLING GEMINI:", e)