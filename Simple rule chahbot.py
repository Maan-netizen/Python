# -*- coding: utf-8 -*-
"""
A Simple Rule-Based Python Chatbot

This script demonstrates how to build a basic chatbot without any external APIs or libraries.
It uses a set of predefined rules (if-elif-else statements) to respond to user input.
This approach does not require an API key or an internet connection.
"""

import datetime

def get_bot_response(user_input):
    """
    Generates a response based on a set of rules.
    """
    # Convert user input to lowercase to make matching easier
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hello there! How can I help you today?"
    
    elif "how are you" in text:
        return "I'm just a program, so I'm doing great! Thanks for asking."
        
    elif "your name" in text:
        return "I am a simple rule-based chatbot created in Python."

    elif "time" in text:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    elif "date" in text:
        today = datetime.date.today()
        return f"Today's date is {today.strftime('%B %d, %Y')}."
        
    elif "help" in text:
        return "You can ask me things like 'what is your name?', 'what time is it?', or just say 'hello'."

    else:
        # Default response if no rules match
        return "I'm not sure how to answer that. Please try asking something else or type 'help'."

def main():
    """
    Main function to run the chatbot application.
    """
    print("--- Simple Chatbot is Ready ---")
    print("You can start chatting now. Type 'exit' or 'quit' to end the session.")
    print("-" * 30)

    # --- Main Chat Loop ---
    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("\nThank you for chatting. Goodbye!")
            break
        
        if not user_input.strip():
            print("Bot: Please say something.")
            continue
        
        # Get the bot's response and print it
        bot_response = get_bot_response(user_input)
        print(f"Bot: {bot_response}")


if __name__ == "__main__":
    main()
