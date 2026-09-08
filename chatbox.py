def chatbot_response(user_input):
    # Convert input to lowercase
    user_input = user_input.lower().strip()

    # Predefined chatbot responses
    if user_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How are you?"

    elif user_input == "what is your name":
        return "I am a Basic Python Chatbot."

    elif user_input == "who created you":
        return "I was created using Python."

    elif user_input == "help":
        return "You can say hello, ask how I am, ask my name, or say bye."

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that. Please try something else."


def start_chatbot():
    print("=" * 50)
    print("       🤖 WELCOME TO BASIC CHATBOT")
    print("=" * 50)
    print("Chatbot: Hello! Type 'bye' to exit.")
    print()

    while True:
        user_input = input("You: ")

        response = chatbot_response(user_input)

        print("Chatbot:", response)

        # Exit condition
        if user_input.lower().strip() in ["bye", "goodbye", "exit"]:
            break


# Start the chatbot
start_chatbot()
