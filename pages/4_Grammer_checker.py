import streamlit as st
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

st.title("🦜 Grammer checker App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
os.environ["OPENAI_API_KEY"] = openai_api_key

def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-4")
    # Prompt
    template = """As a seasoned writer and meticulous proofreader, I need your assistance to enhance the quality of my text. 
    Please carefully review the content, identify any grammatical errors, and apply corrections. 
    Pay close attention to proper conventions, punctuation, and tone to ensure the text reads flawlessly and professionally. 
    Your expertise in refining language will greatly contribute to the overall polish and clarity of the writing.\n\n 
    <my_text>{topic}</my_text>"""
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)


