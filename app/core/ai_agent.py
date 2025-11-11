from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

def get_response_from_ai_agent(llm_id: str, query: list, allow_search: bool, system_prompt: str):
  try:
    llm = ChatGroq(model=llm_id)

    if allow_search:
        search = TavilySearch(max_results=2)
        search_results = search.run({"query": ",".join(query)})
        query = f"{query}\n\nSearch results:\n{search_results}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]

    response = llm.invoke(messages)
    return response.content
  except Exception as e:
    print(e)
