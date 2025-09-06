import speech_recognition as sr
import os

r = sr.Recognizer()

print("Recording... Speak now!")

with sr.Microphone() as source:
    audio = r.listen(source, phrase_time_limit=5)

# Create and save audio file
filename = "test_audio.wav"
with open(filename, "wb") as f:
    f.write(audio.get_wav_data())

print("Saved to:", os.path.abspath(filename))
