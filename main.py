from whisper_mic import transcribe_from_mic
from speak import say
from llm import ask_ai
from memory import log_message

def main():
    print("🤖 Hi! I'm AiVA — your voice assistant.")
    print("🎤 Say something! Say 'quit' or 'exit' to stop.")

    while True:
        user_input = transcribe_from_mic()
        if not user_input:
            print("🤷 I didn’t catch that. Try again.")
            continue

        print("👂 You said:", user_input)
        if user_input.lower() in ["exit", "quit"]:
            break

        log_message("user", user_input)

        response = ask_ai(user_input)
        print("🧠 AiVA:", response)

        log_message("ai", response)

        say(response)

if __name__ == "__main__":
    main()
