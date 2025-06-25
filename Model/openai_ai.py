import openai
import os

import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]

def ask_openai(prompt: str, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You're a COBOL code reviewer who explains the logic in a helpful, accurate way."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content'].strip()