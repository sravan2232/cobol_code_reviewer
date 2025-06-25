import requests
import openai
import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]
#from Model.openai_ai import ask_openai as ask_ai
#def ask_local_ai(prompt, model='mistral'):
#    url = "http://localhost:11434/api/generate"
#    payload = {
#        "model": model,
#        "prompt": prompt,
#        "stream": False
#    }

#    try:
#        response = requests.post(url, json=payload)
#        return response.json()['response'].strip()
#    except Exception as e:
#        return f"❌ Error communicating with local AI: {e}"
# No need to import from Model.openai_ai anymore

def ask_ai(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You're a COBOL code reviewer who explains COBOL programs clearly and thoroughly."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response['choices'][0]['message']['content'].strip()