# Jarvis - Voice-Activated Virtual Assistant

Jarvis is a Python-based voice assistant that listens for your voice commands and performs tasks like opening websites, playing music, reading news, and answering questions using OpenAI's GPT-3.5-turbo. It activates when you say the wake word **"Jarvis"**.

---

##  Key Features

- **Voice Recognition**  
  Uses the `speech_recognition` library to detect voice commands after hearing the wake word **"Jarvis"**.

- **Text-to-Speech**  
  Uses `gTTS` to convert text responses to speech and plays them using `pygame`.

- **Web Browsing**  
  Opens commonly used websites like Google, Facebook, and YouTube.

- **Music Playback**  
  Responds to commands like `play shape` using a custom `musicLibrary.py` file containing song links.

- **News Reading**  
  Fetches and speaks out the latest headlines using NewsAPI.

- **GPT-3.5 Integration**  
  Uses OpenAI's GPT-3.5-turbo for intelligent conversational responses.

---

## Tech Stack & Libraries

- `speech_recognition` – for voice input  
- `gTTS` + `pygame` – for voice output  
- `openai` – to generate responses  
- `requests` – to fetch data from APIs  
- `webbrowser` – to open websites  
- `os`, `time`, `traceback` – for system handling  
- Custom `musicLibrary` module – for music links

---

## Getting Started
1. Install Dependencies
   
  - pip install -r requirements.txt
2. Add Your API Keys
  - openai.api_key = "your_openai_api_key_here"
  - newsapi = "your_news_api_key_here"
3. Add Songs to musicLibrary.py
   Open musicLibrary.py and add entries like:
    music = {
        "shape": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
        "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc"
    }
4. Run Jarvis
   python jarvis.py

**Example Commands**
 "Jarvis" → Wake word
 "Open Google"
 "Play believer"
 "Give me the news"
 "What is Python used for?"

