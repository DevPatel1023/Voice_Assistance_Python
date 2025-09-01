from text_to_speech import jarvis_output_speak as speak
from speech_recognition_fun import transcribe_audio as listen


#Entry point

def main():
   speak("Hello boss , How can i assist you ?")
   while True :
        command = listen()
        if 'stop' in command or 'exit' in command or 'sleep' in command:
            speak("Shutting down systems")
        elif "hello" in command:  
            speak("Hello,how are you?")                     
        elif "time" in command:
                                                     
        


if __name__ == "__main__" : 
    main()