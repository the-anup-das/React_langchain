import streamlit as st
from openai import OpenAI

# Define the available models
available_models = ["gpt-3.5-turbo", "text-davinci-003","gpt-4","gpt-4-1106-preview"]  # Add more models as needed

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    selected_model = st.selectbox("Select Chatbot Model", available_models)

st.title("📝 File Q&A with Anthropic")
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file,
)

if uploaded_file and question and not openai_api_key:
    st.info("Please add your Openai API key to continue.")

if uploaded_file and question and openai_api_key:
    article = uploaded_file.read().decode()
    client = OpenAI(api_key=openai_api_key)
    # Use the selected model
    response = client.chat.completions.create(
        model=selected_model, 
        messages=[
    {"role": "system", "content": f"You are an assistant, skilled in explaining and answering question from the article Here's an article:\n\n<article>
    {article}\n\n</article>"},
    {"role": "user", "content": question}
  ]
        )
    msg = response.choices[0].message.content
    st.write("### Answer")
    st.write(msg)