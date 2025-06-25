import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]
client = openai.OpenAI()

def ask_ai(prompt, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a COBOL code reviewer. Explain COBOL programs clearly and thoroughly for junior developers."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    
    except openai.RateLimitError as e:
        st.error("⚠️ OpenAI Rate Limit Reached. Please check your usage or try again later.")
        return "Rate limit error."
    
    except openai.OpenAIError as e:
        st.error(f"❌ OpenAI API error: {str(e)}")
        return "OpenAI error occurred."
    
    except Exception as e:
        st.error(f"❌ Unexpected error: {str(e)}")
        return "Something went wrong."
