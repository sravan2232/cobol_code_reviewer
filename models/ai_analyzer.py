import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

client = openai.OpenAI()

def ask_ai(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a COBOL code reviewer. Explain COBOL programs clearly and thoroughly for junior developers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
