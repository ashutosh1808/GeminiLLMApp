import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
chat_model=model.start_chat(history=[])

def generate_response(question):
    response=chat_model.send_message(question,stream=True)
    return response

#streamlit app
st.title("Gemini Chat App")
input_prompt=st.text_input("Start chatting",key=input)
submit=st.button("Chat")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

if input_prompt and submit:
    #append prompt and response in history
    response=generate_response(input_prompt)
    st.session_state['chat_history'].append(("You ",input_prompt))
    for chunk in response:
        st.subheader("Your response")
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot ",chunk.text))

#Chat history
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")