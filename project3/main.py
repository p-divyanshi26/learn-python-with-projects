import webbrowser
import speech_recognition as sr
import pyttsx3
import traceback
import time
import musicLibrary
import requests 
from openai import OpenAI
from gtts import gTTS
import pygame
import os


# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0bf68a4893b84214a05e478b7450bcaf"

# Function to speak text

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

# Function to process command
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open(f"https://www.youtube.com") 
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link= musicLibrary.music[song] 
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
        else:
        # Let OpenAI handle the request
         output = aiProcess(c)
         speak(output) 
        
if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
        r = sr.Recognizer()
        print("\n--- Recognizing Wake Word ---")
        
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for 'Jarvis'...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            try:
                word = r.recognize_google(audio)
                print(f"You said: {word}")

                if word.lower() == "jarvis":
                    print("✅ Wake word detected.")
                    speak("Yes, I am listening.")
                    time.sleep(1)  # Give time for mic release before next listen

                    print("Please speak your command now...")

                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source, duration=0.5)
                        print("Listening for command...")
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)

                    command = r.recognize_google(audio)
                    processCommand(command)

            except sr.UnknownValueError:
                print("❌ Could not understand audio.")
            except sr.RequestError as e:
                print(f"⚠️ API error: {e}")

        except sr.WaitTimeoutError:
            print("⏳ Timeout: No wake word detected.")
        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
