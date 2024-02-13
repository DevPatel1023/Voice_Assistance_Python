import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import random
import datetime
import pyjokes
import requests

NEWS_API_KEY = 'Your_APi_Key'

WAKE_WORD = "Hey Jarvis"

def takecommand():
    r = sr.Recognizer()
    r.energy_threshold = 4000  
    r.pause_threshold = 0.5
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
    joke = pyjokes.get_joke()
    say(joke)

def search_the_web(query):
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(search_url)
    say(f"Searching the web for {query}.")



def play_music(file_path):
    os.startfile(file_path)

def get_headlines():
    # Fetch latest news headlines
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": NEWS_API_KEY
    }
    main_url = "https://newsapi.org/v1/articles"

    # Fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    # Getting all articles' titles
    articles = open_bbc_page["articles"]
    headlines = [article["title"] for article in articles][:3]  # Limit to top 3 headlines

    return headlines

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

            elif "what's the news" in query:
                # Fetch latest news headlines
                headlines = get_headlines()

                # Speak out the headlines
                for idx, headline in enumerate(headlines, start=1):
                    print(f"{idx}. {headline}")
                    say(headline)

            elif "what's the time" in query:
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
