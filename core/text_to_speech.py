#convert text -> voice

import pyttsx3 

def jarvis_output_speak(text):
    # init the engine
    engine = pyttsx3.init()
    engine.setProperty("rate",175)
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say("boss : ",text)
    engine.runAndWait();