import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv() #load all envs

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#gemini content
def generate_content(prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt)
    return response.text

#streamlit app
st.title("Gemini LLM App")
input_prompt=st.text_input("Enter something",key=input)
submit=st.button("Submit")

if submit:
    response=generate_content(input_prompt)
    st.write(response)