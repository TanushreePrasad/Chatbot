import random

def greeting():
    print("Hello! Nice to meet you! How can I help you today?")

def farewell():
    print("Thank you for your valuable time. Have a great day!")

def handle_question(question):
    # Mapping of basic questions to responses
    responses = {
        "How can you help?": "I'm here to assist you with any questions you may have.",
        "How do you work?": "I use advanced algorithms to understand and respond to your queries.",
        "Who created you?": "I was created by Tanushree for this project.",
        "Tell me a joke.": "Why did the computer keep its drink on the windowsill? Because it wanted a cold drink!",
        "What can you do?": "I can answer questions, tell jokes, and engage in simple conversations."
    }

    # Check if the question is in the responses mapping
    if question in responses:
        return responses[question]
    else:
        return "I'm sorry, I don't have an answer for that right now. Feel free to ask something else!"

def conversation_flow():
    questions = [
        "How are you today?",
        "What is your favorite sport?",
        "Where are you from?",
    ]

    c=0

    for question in questions:
        c+=1
        user_response = input(question + "\nYour answer: ")
        if c == 1:
            print("Chatbot: That's interesting!")
        elif c == 2:
            print("Chatbot: Great! We can play that together sometime")
        else:
            print("Chatbot: Ohh! Its a great place to stay.")        

def chatbot_main():
    greeting()

    # Implement basic error handling
    try:
        # Implement basic conversation flow
        conversation_flow()

        # Ask user for questions
        for _ in range(3):
            user_question = input("Ask me a question: ")
            response = handle_question(user_question)
            print("Chatbot:", response)

        farewell()
    except KeyboardInterrupt:
        print("\nChatbot: It seems like you want to leave. Goodbye!")

if __name__ == "__main__":
    chatbot_main()
