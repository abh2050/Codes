##integrate our code with OpenAI API
import os
from constant import openai_key
from langchain.llms import OpenAI

import streamlit as st

#streamlit framework
st.title('Langchain Demo With OpenAI API')
input_text = st.text_input('Search the topic you want:')

#OPENAI LLMS
os.environ["OPENAI_API_KEY"] = openai_key
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
    


