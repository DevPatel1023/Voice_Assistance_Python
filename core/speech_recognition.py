#convert voice -> text for (queries)

import speech_recognition as sr

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
            print("Sorry, i dont understand")
        except sr.RequestError:
            print("Network error")

    


