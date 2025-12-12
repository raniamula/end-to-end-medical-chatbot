import streamlit as st
import json
from model.rules import get_prediction

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
import json
import re

def get_prediction(text):
    text = text.lower()

    if any(x in text for x in ["fever", "temperature"]):
        return "Possible Infection / Viral Fever. Stay hydrated and monitor your temperature."

    if any(x in text for x in ["headache", "migraine"]):
        return "Possible Migraine / Stress. Rest, hydrate, avoid bright screens."

    if any(x in text for x in ["cough", "cold", "sore throat"]):
        return "Possible Common Cold or Flu."

    if any(x in text for x in ["chest pain"]):
        return "Serious symptom. Seek medical attention immediately."

    return "I could not identify the condition clearly. Please provide more details."
