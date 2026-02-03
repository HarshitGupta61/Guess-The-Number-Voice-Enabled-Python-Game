import random
import time
import pyttsx3

# ================= SAFE SPEAK FUNCTION =================
def speak(text):
    print("🤖 Jarvis:", text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ================= INTRO =================
def welcome():
    speak("Welcome to the advanced guess the number game.")
    time.sleep(0.5)

# ================= DIFFICULTY =================
def choose_difficulty():
    speak("Choose difficulty. Easy, medium, or hard.")
    while True:
        level = input("Difficulty (easy / medium / hard): ").lower()
        if level == "easy":
            return 50
        elif level == "medium":
            return 100
        elif level == "hard":
            return 500
        else:
            speak("Invalid choice. Try again.")

# ================= GAME =================
def play_game():
    max_num = choose_difficulty()
    number = random.randint(1, max_num)
    attempts = 0

    speak(f"I have selected a number between 1 and {max_num}. Start guessing.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess > number:
                speak("Lower number please.")
            elif guess < number:
                speak("Higher number please.")
            else:
                speak(f"Congratulations. You guessed the number in {attempts} attempts.")
                break

        except ValueError:
            speak("Please enter a valid number.")

# ================= MAIN =================
if __name__ == "__main__":
    welcome()

    while True:
        play_game()
        speak("Do you want to continue playing? Please press yes or no.")
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            speak("Thank you for playing. Goodbye.")
            break
