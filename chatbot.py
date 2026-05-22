print("===== SMART CHATBOT =====")

name = input("Enter your name: ")
print(f"Hello {name}! I am your AI Chatbot.")

while True:
    user = input(f"\n{name}: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hey there! Nice to meet you.")

    elif "how are you" in user:
        print("Bot: I'm functioning perfectly!")

    elif "your name" in user:
        print("Bot: I am an Advanced Python Chatbot.")

    elif "python" in user:
        print("Bot: Python is a powerful programming language.")

    elif "weather" in user:
        print("Bot: I cannot check live weather yet, but it looks like a great day to code!")

    elif "time" in user:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "bye" in user or "exit" in user:
        print(f"Bot: Goodbye {name}! Have a wonderful day.")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")