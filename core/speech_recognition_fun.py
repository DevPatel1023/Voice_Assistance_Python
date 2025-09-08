import speech_recognition as sr
import time

def transcribe_audio():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        time.sleep(0.3)#small buffer before starting mic
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Please speak now...")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Audio captured, transcribing...")
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return None
        except KeyboardInterrupt:
            print("Listening interrupted by user.")
            return None
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"API Error: {e}")
            return None
