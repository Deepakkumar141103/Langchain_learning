from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=1)
                   
st.header('Research Tool')

user_input = st.text_input('enter ur prompt')

if st.button('Summarize'):
    result= model.invoke(user_input)
    st.write(result.content)
