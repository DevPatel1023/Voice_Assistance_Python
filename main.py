from core.text_to_speech import jarvis_output_speak as speak
from core.speech_recognition_fun import transcribe_audio as listen
from core.command_processor import process_command
from core.wake_word import wake_word  # Add wake word function

def main():

    while True:
        
        speak("how can I assist you today?")
        
        while True:
            command = listen()

            if command is None:
                speak("Sorry, I didn't catch that. Can you repeat?")
                continue  # Go back and ask again

            print(command)

            if any(word in command for word in ["stop", "sleep", "shut down", "exit"]):
                speak("Shutting down the system")
                return  # Ends entire assistant

            elif any(word in command for word in ["thank you", "bye"]):
                speak("Okay boss, I'm going back to sleep mode.")
                break  # Goes back to waiting for wake word
            else:
                process_command(command, speak, listen)


if __name__ == "__main__":
    main()
