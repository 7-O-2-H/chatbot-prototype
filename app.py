# App dev framework 
import streamlit as st

#Import dependencies
from langchain.llms import GPT4All
from langchain import PromptTemplate, LLMChain

# Path to weights
PATH = '/Users/joshkelly/Library/Application Support/nomic.ai/GPT4All/mistral-7b-openorca.Q4_0.gguf'

llm = GPT4All(model=PATH, verbose=True)

# Prompt template
prompt = PromptTemplate(input_variables=['question'],
                        template="""
                        Question: {question}
                        
                        Answer: Let's think that through step by step
                        """)

# LLM Chain
chain = LLMChain(prompt=prompt, llm=llm)
# Title
st.title('AI-Project')

# Prompt text box
prompt = st.text_input('Input prompt here')

if prompt:
  #Pass prompt
  res = chain.run(prompt)

  st.write(res)