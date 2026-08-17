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

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama3-70b-8192",
    api_key="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"
)

res = llm.invoke("What is the Capital of Pakistan?")
print(res)