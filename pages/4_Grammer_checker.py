import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("🦜 Fix Grammer in your text")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(paragraph, openai_api_key):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-4-1106-preview", openai_api_key=openai_api_key)
    # Prompt
    template = """As a seasoned writer and meticulous proofreader, I need your assistance to enhance the quality of my text. 
    Please carefully review the content, identify any grammatical errors, and apply corrections. 
    Pay close attention to proper conventions, punctuation, and tone to ensure the text reads flawlessly and professionally. 
    Your expertise in refining language will greatly contribute to the overall polish and clarity of the writing.\n\n 
    <my_text>{paragraph}</my_text>"""
    prompt = PromptTemplate(input_variables=["paragraph"], template=template)
    prompt_query = prompt.format(paragraph=paragraph)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter your text:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text, openai_api_key)