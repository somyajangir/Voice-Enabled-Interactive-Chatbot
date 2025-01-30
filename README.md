# 🎤 Voice-Enabled Interactive Chatbot 🤖

Welcome to the **Voice-Enabled Interactive Chatbot**! 🚀 This is a **voice-to-voice** chatbot that uses **Gemini Flash 1.5** to provide intelligent, dynamic responses. It listens to your speech, sends your question to the Gemini API, and responds to you with voice. It's designed to make chatting more natural and engaging. 🗣️💬

## 🚀 Features:
- **🎤 Voice-to-Voice Interaction**: Speak to the chatbot, and it will respond using text-to-speech (TTS).
- **🔄 Context-Aware Conversations**: The chatbot remembers the last few questions you've asked, providing more relevant responses based on previous conversations.
- **⚡ Easy API Setup**: Simply provide your own Gemini API key to start using the bot.
- **💾 Chat History Database**: All conversations are saved in a `conversation_history.json` file, allowing you to keep track of the chatbot's past interactions.

## 📁 Project Structure:
```
Voice-Enabled-Interactive-Chatbot/
├── helpers/
│   └── database.py
├── main.py
├── .env
└── conversation_history.json
```

## 🛠️ Installation:

### 1️⃣ Clone the Repository:
Clone the repository to get started:
```bash
git clone https://github.com/somyajangir/Voice-Enabled-Interactive-Chatbot.git
```

### 2️⃣ Install Dependencies:
You'll need the following libraries:
- `speech_recognition` 📡
- `pyttsx3` 🔊
- `google-generativeai` 🧠
- `python-dotenv` 🔒

Install them using pip:
```bash
pip install speech_recognition pyttsx3 google-generativeai python-dotenv
```

### 3️⃣ Set Up Your Gemini API Key:
To use the Gemini API, you'll need to set up your API key:
- Get your gemini-1.5-flash API key from Google AI Studio.
- Create a `.env` file in the root directory and add your API key like this:
```env
GEMINI_API_KEY=your-api-key-here
```

### 4️⃣ Run the Chatbot:
Now you are ready to interact with the chatbot. Run the following command to start the bot:
```bash
python main.py
```

### 5️⃣ Start Chatting! 🎉
The chatbot will prompt you to speak your question, and it will reply using text-to-speech.

## 🤔 How it Works:
- 🎧 **Speech Recognition**: The chatbot listens to your voice using the `speech_recognition` library.
- ⚡ **Gemini API**: Your question is sent to the Gemini API, which generates a response.
- 🔊 **Voice Output**: The response is spoken back to you using the `pyttsx3` library.
- 🔁 **Context**: The chatbot remembers your previous questions, so conversations feel more fluid and context-aware.
- 💾 **Chat History**: All your interactions are stored in a `conversation_history.json` file. This allows you to review past conversations and track your interaction history.

### 🤖 License:
This project is open-source and freely available for anyone to use, modify, and distribute.
