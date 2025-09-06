#convert voice -> text for (queries)

import speech_recognition as sr
from core.text_to_speech import jarvis_output_speak

# Create speech recognizer
r = sr.Recognizer()

def transcribe_audio():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=1)  # 1 second to calibrate noise
        print("Listening...")
        audio_listened = r.listen(source)
        try:
            query = r.recognize_google(audio_listened)
            return query.lower()
        except sr.UnknownValueError:
            jarvis_output_speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            jarvis_output_speak("Network error, please check your connection.")
            return ""
