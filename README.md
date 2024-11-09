# Voice-Enabled Interactive Chatbot

This is a **voice-to-voice chatbot** that uses **Gemini Flash 1.5** to provide intelligent responses. It recognizes your speech, sends your question to the Gemini API, and then responds to you with voice.

## Features:

- **Voice-to-Voice Interaction**: Speak to the chatbot, and it will respond using text-to-speech (TTS).
- **Context-Aware Conversations**: The chatbot remembers the last few questions you've asked, providing more relevant responses based on previous conversations.
- **Easy API Setup**: Simply provide your own Gemini API key to start using the bot.
- **Chat History Database**: All conversations are saved in a `conversation_history.json` file, allowing you to keep track of the chatbot's past interactions.

## Installation:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/somyajangir/Voice-Enabled-Interactive-Chatbot.git
Install Dependencies: You’ll need the following libraries:

speech_recognition
pyttsx3
google-generativeai
python-dotenv
Install them using pip:

bash
Copy code
pip install speech_recognition pyttsx3 google-generativeai python-dotenv
Set Up Your Gemini API Key:

Get your Gemini API key from Google Cloud.
Create a .env file in the root directory and add your API key:
env
Copy code
GEMINI_API_KEY=your-api-key-here
Run the Chatbot:

bash
Copy code
python main.py
Start chatting!: The chatbot will ask you to speak your question, and it will reply using text-to-speech.

How it Works:
Speech Recognition: The chatbot listens to your voice using the speech_recognition library.
Gemini API: Your question is sent to the Gemini API, and it generates a response.
Voice Output: The response is then spoken back to you using the pyttsx3 library.
Context: The chatbot remembers your previous questions for more fluid, context-aware conversations.
Chat History: All your interactions with the chatbot are stored in a conversation_history.json file. This database helps track the conversation, and you can review the stored chat history.
