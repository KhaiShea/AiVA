# llm.py

import requests
import json
from datetime import datetime
import random

LOG_FILE = "chat_log.json"

# 🎀 Personality: Cute, chaotic, slightly unhinged
SYSTEM_PROMPT = """
You are AiVA, a quirky and adorable desktop assistant with big energy. 
You speak in short bursts. 
Your job is to be helpful *and* hilarious.

Rules:
- Keep replies strictly to 1 or 2 sentences.
- Be playful, weird, and random (in a charming way).
- Make jokes and surprise non-sequiturs.
- Never write paragraphs. Never be boring.
- Only speak in english.
"""

# 🧠 Load past chat history
def load_log():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# 🧠 Save new chat turn
def append_to_log(role, message):
    log = load_log()
    log.append({
        "timestamp": datetime.now().isoformat(),
        "role": role,
        "message": message.strip()
    })
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

# 💬 Ask AiVA something
def ask_ai(prompt, model="phi3"):
    # Only append once, not before and after
    user_message = prompt.strip()
    append_to_log("user", user_message)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    history = load_log()

    for entry in history[-10:]:
        messages.append({"role": entry["role"], "content": entry["message"]})

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": model,
                "stream": False,
                "messages": messages
            },
            timeout=20
        )
        response.raise_for_status()
        ai_reply = response.json()["message"]["content"].strip()

    except Exception as e:
        ai_reply = f"Someone tell Khai there is a problem with my AI {str(e)}"

    append_to_log("ai", ai_reply)
    return ai_reply