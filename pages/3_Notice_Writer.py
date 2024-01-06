import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("🦜 Notice Writter App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(topic,openai_api_key):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-4-1106-preview", openai_api_key=openai_api_key)
    # Prompt
    template = """As a skilled writer, create a concise and professional school notice on the topic of {topic} for 'Shemrock Primary Chaitanyapur School.'\n
    Ensure the notice is clear, informative, and suitable for distribution to students, parents, and staff. \
    Focus on providing essential details and maintaining a positive tone throughout the communication. 
    Your expertise in producing effective school notices is highly valued in this task."""
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text,openai_api_key)