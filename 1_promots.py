import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the model
model = ChatOpenAI()

st.header("Research Tool") 
user_input = st.text_input("Enter your research question:")

if st.button("Submit") and user_input:
    response = model.invoke(user_input)
    st.write(response.content)
