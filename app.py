# app.py

import streamlit as st
from transformers import pipeline, set_seed

# Title
st.title("EduBot – AI Tutor for Personalized Learning")

# Instructions
st.write("Ask EduBot a question or enter a topic to receive an explanation and a quiz.")

# Input
user_input = st.text_input("Enter your topic/question:")

# Load generator model
generator = pipeline("text-generation", model="gpt2")
set_seed(42)

# Generate Output
if user_input:
    st.subheader("AI-Generated Explanation")
    explanation = generator(user_input, max_length=100, num_return_sequences=1)
    st.write(explanation[0]["generated_text"])

    st.subheader("AI-Generated Quiz")
    quiz_prompt = f"Create a multiple choice question about: {user_input}"
    quiz = generator(quiz_prompt, max_length=80, num_return_sequences=1)
    st.write(quiz[0]["generated_text"])
