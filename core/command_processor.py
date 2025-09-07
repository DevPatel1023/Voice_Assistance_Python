from productivity.datetime_fun import get_time, get_date
from modules.productivity import add_notes, clear_notes, read_notes
from modules.news_weather import get_news, get_weather


def process_command(command: str, speak, listen):
    command = command.lower()
    print("test command process fun reached")
    
    # Time
    if "time" in command:
        speak(f"Boss, the time is {get_time()}")

    # Date
    elif "date" in command:
        speak(f"Boss, the date is {get_date()}")

    # Notes
    elif "note" in command:
        if "add" in command:
            speak("What should I note down, boss?")
            note = listen()
            if note:
                speak(add_notes(note))
        elif "read" in command or "show" in command:
            speak(read_notes())
        elif "clear" in command or "delete" in command or "remove" in command:
            speak(clear_notes())
        else:
            speak("Boss, please say add note, read note, or clear notes.")

    # Weather
    elif "weather" in command:
        print("reach to weather")
        print("DEBUG: About to ask for city...")
        speak("Which city boss")
        print("DEBUG: Asked for city")
        city = listen()
        print(f"DEBUG: Got city: {city}")
        if city:
            speak(f"Weather for {city} is sunny")

    # News
    elif "news" in command:
        speak("Boss, which category of news do you want? Technology, sports, health, or general?")
        topic = listen()
        if topic:
            speak(get_news(topic))

    # Default
    else:
        speak("I am still learning, boss.")
