from core.text_to_speech import jarvis_output_speak as speak
from core.speech_recognition_fun import transcribe_audio as listen
from productivity.datetime_fun import get_time,get_date
from modules.productivity import add_notes,read_notes,clear_notes
from modules.news_weather import get_news

#Entry point

def main():
   speak("Hello boss , How can i assist you ?")
   while True :
        command = listen()
        if 'hey jarvis' in command:
            speak("hello boss , how can i assist you today?")
        elif 'stop' in command or 'exit' in command or 'sleep' in command:
            speak("Shutting down systems")
        elif "hello" in command:  
            speak("Hello,how are you?")                     
        elif "time" in command:
            time = get_time()   
            speak(time)    
        elif "date" in command: 
            date = get_date()
            speak(f"boss the date is ,{date}")      
        elif "note" in command:
            if "add" in command:
                speak("what should i note down ,boss?")
                note = listen()
                if note: 
                    res = add_notes(note)
                    speak(res)
            elif "show" or "read" in command:
                notes = read_notes()
                speak(f"here are your notes : {notes}")
            elif "clear" or "erase" in command:
                res = clear_notes()
                speak(res)
            else:
                speak("Boss , what would you like  add notes , read notes or clear notes.")
        elif "news" or "find about" in command:
            speak("Boss , describe category technology,sports,health or general")
            topic = listen()
            #if should not be empty
            if topic :
                news_report = get_news(topic)
                speak(f"the information is:  {news_report}")

if __name__ == "__main__" : 
    main()