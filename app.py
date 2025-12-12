import streamlit as st
import json
from chat_model.rules import get_prediction

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")

st.title("🩺 Medical Chatbot")
st.write("Describe your symptoms and I will try to help.")

user_input = st.text_area("Enter your symptoms here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.error("Please enter symptoms!")
    else:
        result = get_prediction(user_input)
        st.success(result)
