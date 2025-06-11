from whisper_mic import transcribe_from_mic
from llm import ask_ai
from speak import say

def main():
    print("🤖 Hi! I'm AiVA — your voice assistant.")
    print("🎤 Say something! Say 'quit' or 'exit' to stop.")

    while True:
        user_input = transcribe_from_mic()
        if not user_input:
            print("🤷 I didn’t catch that. Try again.")
            continue

        user_input = user_input.strip().lower()
        if user_input in ['quit', 'exit']:
            print("👋 Goodbye!")
            break

        print(f"👂 You said: {user_input}")
        response = ask_ai(user_input)
        print(f"🧠 AiVA: {response}")
        say(response)

if __name__ == "__main__":
    main()
