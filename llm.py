import requests

def ask_ai(prompt):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "⚠️ There was a problem contacting the AI."
