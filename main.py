from helpers.database import save_conversation_entry, get_last_question

import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Ensure GEMINI_API_KEY is set in your environment or .env file.")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def recognize_speech():
    """Recognize speech from the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your question...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        query = recognizer.recognize_google(audio)
        print(f"You asked: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
    return None

def query_gemini(question, context=None):
    """Send the user's question to the Gemini API and return the response."""
    try:
        # Update the prompt to be more interactive
        prompt = (
            "Just answer in an interactive way based on what the user asks. "
            "Avoid using asterisks and hashtags. Keep the response short, as the user will be listening rather than reading."
        )
        
        if context:
            complete_query = f"{prompt} Previous question: '{context}'. Current question: '{question}'"
        else:
            complete_query = f"{prompt} {question}"

        response = model.generate_content(complete_query)
        return response.text
    except Exception as e:
        print(f"An error occurred while querying Gemini: {e}")
    return None

def speak_response(response):
    """Convert the response text to speech."""
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

def provide_default_prompt():
    """Provide a default prompt for the user."""
    prompt = "Ask me anything"
    print(prompt)
    speak_response(prompt)

def main_loop():
    """Main loop to keep the chatbot running and responding to user queries."""
    provide_default_prompt()  # Provide the default prompt before listening

    last_questions = []  # Initialize a list to keep track of the last three questions

    while True:
        query = recognize_speech()
        if query:
            # Add the current query to the list of last questions
            last_questions.append(query)
            
            # Keep only the last three questions
            if len(last_questions) > 3:
                last_questions.pop(0)

            # Use the last three questions as context
            context = " | ".join(last_questions[:-1])  # Join the last two questions for context

            gemini_response = query_gemini(query, context)
            if gemini_response:
                print(f"Response: {gemini_response}")  # Print the response to the console
                speak_response(gemini_response)  # Convert the response to speech
                
                # Save the question and response to history
                save_conversation_entry(query, gemini_response)

            # Optional: Check for an exit command
            if query.lower() in ["exit", "stop"]:
                print("Exiting the chatbot. Have a great day!")
                break

if __name__ == "__main__":
    main_loop()

