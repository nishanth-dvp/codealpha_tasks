def chatbot(message):
    if message == "hello":
        return "Hi!"
   
    if message== "hi":
        return "Hello!"
    
    if message == "how are you":
        return "I'm fine, thanks!"

    if message == "bye":
        return "Goodbye!"
    
    if message == "what is your name":
        return "I am a chatbot."

    else:
        return "Sorry, I don't understand."


print("===== Basic Chatbot =====")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    reply = chatbot(user)

    print("Bot:", reply)

    if user == "bye":
        break