import streamlit as st
from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
import os

st.title("🦜 Notice Writter App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
os.environ["OPENAI_API_KEY"] = openai_api_key

def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-4")
    # Prompt
    template = """As a skilled writer, create a concise and professional school notice on the topic of {topic} for 'Shemrock Primary Chaitanyapur School.'\n
    Ensure the notice is clear, informative, and suitable for distribution to students, parents, and staff. \
    Focus on providing essential details and maintaining a positive tone throughout the communication. 
    Your expertise in producing effective school notices is highly valued in this task."""
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)