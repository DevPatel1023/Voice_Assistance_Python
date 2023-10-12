import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import random
import datetime

WAKE_WORD = "Hey Jarvis"

def takecommand():
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            print("Listening...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)
            return "Some error occurred"



def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def tell_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I'm reading a book on anti-gravity. It's impossible to put down!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fish with no eyes? Fsh",
        "I told my computer I needed a break, and now it won't stop sending me Kit Kat bars.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I don't trust stairs because they're always up to something."
    ]
    say(random.choice(jokes))


def search_the_web(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    say(f"Searching the web for {query}.")

def play_music(file_path):
    os.startfile(file_path)

if __name__ == "__main__":
    assistant_activated = False

    while True:
        print("Listening...")
        query = takecommand().lower()

        if WAKE_WORD.lower() in query.lower() and not assistant_activated:
            assistant_activated = True
            say("Hello, I am your voice assistant. How can I assist you today?")

        if assistant_activated:

            if "stop" in query:
                assistant_activated = False
                say("Jarvis deactivated.")

            elif "tell me a joke" in query:
                tell_joke()

            elif "search the web for" in query:
                query_parts = query.split("search the web for")
                if len(query_parts) > 1:
                    search_query = query_parts[1].strip()
                    search_the_web(search_query)

            elif "play music" in query:
                music_file_path = "C:/Users/Dev/Downloads/Kaleo - Way Down We Go.mp3"
                play_music(music_file_path)

            elif "the time" in query:
                current_datetime = datetime.datetime.now()
                current_time = current_datetime.time()
                say(f"Sir time is: {current_time}")

            elif "open" in query:
                for website in ["google", "youtube", "spotify", "github", "hotstar", "facebook", "twitter", "instagram",
                                "whatsapp", "wikipedia", "zomato", "ola", "netflix"]:
                    if website in query:
                        web_url = website + ".com"
                        webbrowser.open(web_url)
                        say(f"Opening {website} ...")
                        break
                else:
                    say("Website is not found")
