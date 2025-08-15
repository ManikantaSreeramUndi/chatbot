import sys

def run_chatbot():

    print("Hello! I'm a simple rule-based chatbot.")
    print("You can say 'hello', 'how are you', 'your name', or 'bye' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if "hello" in user_input:
            print("Chatbot: Hi there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, so I don't have feelings, but I'm ready to chat!")
        elif "your name" in user_input:
            print("Chatbot: I don't have a name, but you can call me Chatbot.")
        elif "weather" in user_input:
            print("Chatbot: I cannot provide real-time weather information, as I am a simple rule-based bot.")
        elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure I understand that. Can you please rephrase?")

if __name__ == "__main__":
    run_chatbot()