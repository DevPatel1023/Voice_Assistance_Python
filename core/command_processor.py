from productivity.datetime_fun import get_time, get_date
from modules.productivity import add_notes, clear_notes, read_notes
from modules.news_weather import get_news, get_weather


def process_command(command: str, speak, listen):
    command = command.lower()
    
    try :
        # Time
        if "time" in command:
            print(f'time cmd reach {get_time()}')
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
            print("Reached weather command")
            speak("Which city boss?")
            city = listen()
            print(f"DEBUG: User said city: {city} (type: {type(city)})")
    
            if city:
                try:
                    weather = get_weather(city)
                    print(f"DEBUG: Weather returned: {weather}")
                    speak(weather)
                except Exception as e:
                    print(f"ERROR: Failed to get weather: {e}")
                    speak("Sorry boss, I couldn't get the weather.")
                else:
                    print("DEBUG: No city was captured.")
                    speak("I didn't catch the city name, boss.")

        # News
        elif "news" in command:
            speak("Boss, which category of news do you want? Technology, sports, health, or general?")
            topic = listen()
            if topic:
                speak(get_news(topic))

        # Default
        else:
            speak("I am still learning, boss.")

    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        speak("Sorry boss, something went wrong.")
