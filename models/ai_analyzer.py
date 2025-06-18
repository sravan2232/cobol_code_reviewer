import requests

def ask_local_ai(prompt, model='mistral'):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)
        return response.json()['response'].strip()
    except Exception as e:
        return f"❌ Error communicating with local AI: {e}"