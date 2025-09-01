#convert voice -> text for (queries)

import speech_recognition as sr
from text_to_speech import jarvis_output_speak

#create a speech recognition object
r = sr.Recognizer()

def transcribe_audio():
    #use audio 
    with sr.Microphone() as source:
        print("Listening...")
        # record voice
        audio_listened = r.listen(source)
        try:
            query = r.recognize_google(audio_listened)
            return query.lower()
        except sr.UnknownValueError:
            jarvis_output_speak("Sorry, i dont understand")
        except sr.RequestError:
            jarvis_output_speak("Network error")


