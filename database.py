import json
from datetime import datetime

# File to store conversation history
HISTORY_FILE = 'conversation_history.json'

def load_conversation_history():
    """Load conversation history from JSON file."""
    try:
        with open(HISTORY_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file does not exist
    except json.JSONDecodeError:
        print("Error decoding JSON. Initializing an empty history.")
        return []  # Return an empty list if JSON is not valid

def save_conversation_entry(question, response):
    """Save a new entry to the conversation history."""
    entry = {
        'question': question,
        'response': response,
        'timestamp': datetime.now().isoformat()  # Save current timestamp
    }
    history = load_conversation_history()
    history.append(entry)  # Append new entry
    
    with open(HISTORY_FILE, 'w') as file:
        json.dump(history, file, indent=4)  # Save updated history

def get_last_question():
    """Retrieve the last question from the conversation history."""
    history = load_conversation_history()
    if history:  # Check if history is not empty
        return history[-1]['question']  # Return the last question
    return None  # Return None if there are no questions
