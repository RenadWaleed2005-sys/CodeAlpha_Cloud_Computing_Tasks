import sys

def get_bot_response(user_message):
    message = user_message.lower().strip()
    
    if "hello" in message or "hi" in message or "أهلا" in message:
        return "Hello! Welcome to our Cloud Solutions Support. How can I help you today?"
    
    elif "services" in message or "pricing" in message or "خدمات" in message:
        return "We offer Cloud Hosting, Automated Backups, and Data Security Systems with flexible monthly plans."
    
    elif "support" in message or "help" in message or "دعم" in message:
        return "Our technical support team is available 24/7. You can open a ticket at support@cloudcompany.com."
    
    elif "security" in message or "safe" in message or "أمان" in message:
        return "All our cloud storage plans are protected using AES-256 end-to-end encryption."
    
    elif "exit" in message or "bye" in message or "شكرا" in message:
        return "Thank you for using our Cloud Support Chatbot. Have a great day!"
        
    else:
        return "I'm sorry, I didn't quite catch that. Could you please rephrase your question or type 'support' to reach a human agent?"

def start_chatbot():
    print("==================================================")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["exit", "bye", "quit"]:
            print(f"Bot: {get_bot_response(user_input)}")
            break
            
        response = get_bot_response(user_input)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    start_chatbot()

