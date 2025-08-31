#convert text -> voice

import pyttsx3 

def jarvis_output_speak(text):
    # init the engine
    engine = pyttsx3.init()
    engine.say("boss : ",text)
    engine.runAndWait();