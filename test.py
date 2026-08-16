from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# res = tavily_search("what is the capital of Pakistan?")
# print(res)

res = search_flights("Plan a 7 days Dubai trip from Pakistan")
print(res)
