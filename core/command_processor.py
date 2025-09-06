#parse & execute commands
from productivity.datetime_fun import get_time,get_date
from modules.productivity import add_notes,clear_notes,read_notes
from modules.news_weather import get_news , get_weather 

def process_command(command : str , speak ,listen) :
    command = command.lower()

    #time 
    if "time" in command :
        speak(get_time()) 
           
    #date
    elif "date" in command :
        speak(f"Boss the date is ,get_date()") 
    
    #Notes
    elif "Note" in command :
        if "add" in command :  
            speak("What should i note down boss?")
            note = listen()
            if note :
                speak(add_notes(note))
        elif "read" or "show" in command : 
            speak(read_notes())
        elif "clear" or "delete" or "remove" in command :   
            speak(clear_notes())
        else :
            speak("Boss , please say add note , read note or clear notes.")


    elif "weather" in command :
        speak("which city boss?")
        city = listen()
        if city :
            speak(get_weather())

    elif "news" in command:
        speak("Boss ,which category of news do you want to hear about technology,sports,health or general ?")
        topic = listen()
        if topic:
            speak(get_news(topic))

    else :
        speak("I am still learning , boss")