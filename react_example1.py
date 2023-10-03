from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

OPENAI_KEY =""

llm = OpenAI(openai_api_key=OPENAI_KEY, temperature=0)

tools = load_tools(["serpapi","llm-math"], llm = llm)

agent  = initialize_agent(tools, llm, agent = AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)