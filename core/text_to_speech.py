#convert text -> voice

import pyttsx3
import time

# Initialize once
engine = pyttsx3.init()
engine.setProperty("rate", 175)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def jarvis_output_speak(text : str):
    print("speak fun")
    engine.say(f"Boss: {text}")
    engine.runAndWait()
    time.sleep(0.5)# small pause to ensure audio device reset
    print("is it work?")
