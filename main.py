# main.py
import threading
import time
from whisper_mic import transcribe_from_mic
from llm import ask_ai
from speak import say

listening = False

def run_conversation_loop(callback=None):
    global listening
    listening = True

    while listening:
        print("🎤 Recording for 5 seconds. Please speak now...")
        user_input = transcribe_from_mic()

        if not user_input.strip():
            print("🤷 I didn’t catch that. Try again.")
            continue

        print(f"👂 You said: {user_input}")
        response = ask_ai(user_input)
        print(f"🧠 AiVA: {response}")
        say(response)

        if callback:
            callback(user_input, response)

def stop_conversation():
    global listening
    listening = False
