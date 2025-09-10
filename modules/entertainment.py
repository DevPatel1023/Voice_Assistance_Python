import pyjokes
import random

def tell_joke():
    return pyjokes.get_joke()

def guess_the_number(number : int , speak ,listen):
    speak("Welcome to Guess the Number game! I have selected a number between 1 and 100. Try to guess it!")
    number = random.randint(1,100)
    attempts = 0 
    while True : 
        speak("take a guess")
        guess_text = listen()
        try:
            guess = int(guess_text)
            attempts += 1
            if guess < number:
                speak("Too low! Try again.")
            elif guess > number:
                speak("Too high! Try again.")
            else:
                speak(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
        except ValueError:
            speak("Please say a valid number.that is ranging from 1 to 100.")

def play_rock_paper_scissors(user_choice : str , speak):
    choices = ['rock', 'paper', 'scissors']
    if user_choice not in choices:
        speak("Invalid choice! Please choose rock, paper, or scissors.")
        return
    computer_choice = random.choice(choices)
    speak(f"I chose {computer_choice}.")
    if user_choice == computer_choice:
        speak("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or 
         (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper'):
        speak("You win!")
    else:
        speak("I win!")
    return computer_choice