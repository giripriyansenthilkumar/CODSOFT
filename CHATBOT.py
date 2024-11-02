
def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hey! What's up?"
    elif "my name" in user_input:
        return name
    elif "what can you do" in user_input or "what is your purpose" in user_input:
        return "I'm here to chat, answer questions, and just be a friend! What do you want to talk about?"
    elif "what's your name" in user_input or "your name" in user_input:
        return "My name is chatty"
    elif "how are you" in user_input:
        return "I'm good, thanks for asking! How about you?"
    elif "time" in user_input or "current time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        return f"{current_time}."
    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%B %d, %Y")
        return f"{current_date}."
    elif "favorite color" in user_input:
        return "My favourite colour is black. What about you?"
    elif "movie" in user_input:
        return "Movies are fun and thrill! Seen any good ones lately?"
    elif "joke" in user_input or "make me laugh" in user_input:
        return "The doctor tells the patient to have tablet on 9'o clock but he takes at 6'0 clock. The doctor asks why should you take at 6'0 clocks. The patient replies that he had surpried the disease"
    elif "advice" in user_input:
        return "Never stop learning!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Catch you later! It was fun chatting."
    else:
        return "Hmm, I'm not sure I got that"
name=input("Your name: ")
print("Chatbot: Hey there! Type 'bye' whenever you want to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Catch you later!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
