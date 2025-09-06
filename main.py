from core.text_to_speech import jarvis_output_speak as speak
from core.speech_recognition_fun import transcribe_audio as listen
from core.command_processor import process_command
from core.wake_word import detect_wake_word as wake_word  # Add wake word function

def main():
    speak("Tell me the wake word")

    while True:
        # Wait for wake word
        wake_command = listen()

        if wake_word(wake_command):  # Check if wake word detected
            speak("Hello boss, how can I assist you today?")

            while True:
                command = listen()

                if any(word in command for word in ["stop", "sleep", "shut down", "exit"]):
                    speak("Shutting down the system")
                    return  # Ends entire assistant

                elif any(word in command for word in ["thank you", "bye"]):
                    speak("Okay boss, I'm going back to sleep mode.")
                    break  # Goes back to waiting for wake word

                else:
                    process_command(command, speak, listen)
