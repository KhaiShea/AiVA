from llm import ask_ai

while True:
    try:
        user_input = input("🧪 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = ask_ai(user_input)
        print("🤖 AiVA:", response)
    except KeyboardInterrupt:
        print("\n👋 Bye bye!")
        break
