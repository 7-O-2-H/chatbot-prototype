# App dev framework 
import streamlit as st

#Import dependencies
from langchain.llms import GPT4All

#Python imports
from langchain_experimental.agents.agent_toolkits.create_python_agent import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
# Path to weights
PATH = '/Users/joshkelly/Library/Application Support/nomic.ai/GPT4All/mistral-7b-openorca.Q4_0.gguf'

# LLM instance
llm = GPT4All(model=PATH, verbose=True)

# Python Agent
python_agent = create_python_agent(llm-llm, tool=PythonREPLTool(), verbose=True)
# Title

st.title('AI-Project')

# Prompt text box
prompt = st.text_input('Input prompt here')

if prompt:
  #Pass prompt
  res = python_agent.run(prompt)

  st.write(res)