# 🎯 Guess The Number – Voice Enabled Python Game

A voice-enabled Guess the Number game built using Python.
The game interacts with the player using both text input and text-to-speech (TTS), making it more engaging than a standard CLI game.

# 🚀 Features

🔢 Random number generation

🎚 Difficulty levels:

Easy → 1–50

Medium → 1–100

Hard → 1–500

🗣 Voice feedback using pyttsx3

🔁 Replay option after each game

❌ Input validation for incorrect values

🧠 Clean and modular code structure

# 🛠 Tech Stack

**Language: Python 3**

**Libraries:**

    random

    time

    pyttsx3 (Text-to-Speech)

# 📦 Installation & Setup
1️⃣ Clone the repository

git clone https://github.com/HarshitGupta61/Guess-The-Number-Voice-Enabled-Python-Game

pip install pyttsx3

# Run the game
python guess_game.py

💡Note:- Make sure your system speakers or headphones are enabled for voice output.

# 🎮 How to Play

# Choose a difficulty level: Easy, Medium, or Hard

# Guess the number selected by the system

# The game will guide you using voice hints:

    “Higher number please”

    “Lower number please”

# After winning, choose whether to play again

# 📂 Project Structure
guess-the-number-voice-game/
│
├── guess_game.py      # Main game file
├── README.md          # Project documentation
├── requirements.txt   # Dependencies
└── .gitignore