#convert text -> voice

import pyttsx3

# Initialize once
engine = pyttsx3.init()
engine.setProperty("rate", 175)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def jarvis_output_speak(text):
    engine.say(f"Boss: {text}")
    engine.runAndWait()
