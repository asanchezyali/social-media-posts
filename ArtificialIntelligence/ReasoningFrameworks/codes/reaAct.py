from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

# Simulated search tool
def search_web(query):
    # This would connect to a real API in production
    if "capital of France" in query.lower():
        return "The capital of France is Paris."
    return "No specific information found."

search_tool = Tool(
    name="WebSearch",
    func=search_web,
    description="Searches for up-to-date information."
)

# Initialize ReAct agent with the tool
llm = OpenAI(temperature=0.5)
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent_type="react",
    verbose=True
)

# Example: "What is the capital of France, and its population?"