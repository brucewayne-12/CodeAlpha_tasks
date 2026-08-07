def get_response(user_input):
    
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif text in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif text in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple chatbot!"
    elif text == "":
        return "Please say something!"
    else:
        return "Sorry, I don't understand that. Try 'hello', 'how are you', or 'bye'."


def chat():
   
    print("Chatbot: Hi! Type 'bye' to end our chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        if user_input.lower().strip() in ("bye", "goodbye", "exit", "quit"):
            break



chat()