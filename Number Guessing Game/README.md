*Mitchel’s Number Guessing Game 🎲*

Welcome to Mitchel’s Number Guessing Game—the Python-based, Pygame-powered guessing challenge where you match wits with a randomly chosen number! This colorful game lets you set your difficulty and then challenges you to guess the number within a limited number of attempts. Can you find the right answer before your chances run out?

🕹️ How to Play

	1.	Choose Your Difficulty:
	•	Easy (10 attempts)
	•	Medium (5 attempts)
	•	Hard (3 attempts)
Each difficulty level gives you fewer attempts to guess the number, making it more challenging as you move up!
	2.	Guess the Number:
	•	After selecting a difficulty, a secret number between 1 and 10 is randomly generated.
	•	Enter your guesses into the input box.
	•	Each guess tells you if you’re “Too High” or “Too Low,” so you can zero in on the answer.
	3.	Win or Lose:
	•	If you guess correctly within the allowed attempts, you win!
	•	Run out of attempts? You’ll see the answer and can try again.

🎨 Key Features

	•	Color-coded Buttons:
	•	Difficulty levels are represented with distinct colors for easy recognition:
	•	Green for Easy
	•	Blue for Medium
	•	Red for Hard
	•	Dynamic Feedback:
	•	You’ll get real-time messages about whether your guess was correct or incorrect, helping you adjust each guess accordingly.
	•	Attempts Display:
	•	The number of attempts left is shown in the top-right corner, so you can always check how many tries remain.
	•	Custom Font & Background:
	•	Styled with a sleek custom font and background image for a more engaging experience.

💻 Setup and Installation

Prerequisites

Make sure you have Python 3 and Pygame installed.

To install Pygame, run:

pip install pygame

Running the Game

	1.	Clone or download the repository.
	2.	Open a terminal and navigate to the project directory.
	3.	Run the game with:

python number_guessing_game.py



Enjoy watching your number guesses come to life with color-coded hints and a fun, interactive UI!

🛠️ Game Logic Overview

The game uses Pygame to create an interactive interface and handle the main game loop. Here’s the logic flow:

	•	Random Number Generation: A secret number is generated based on the selected difficulty.
	•	Guess Handling: Player guesses are evaluated, with instant feedback to help guide each guess.
	•	Feedback and Win/Lose Conditions: Game messages update based on the accuracy of each guess, and the game displays a win or loss message accordingly.

🎨 Colors & UI

Colors play a key role in making gameplay intuitive:

	•	Difficulty Levels: Green, Blue, and Red buttons make each level distinct.
	•	Attempts & Messages: Feedback messages keep you informed of your progress and remaining attempts, with each detail designed to enhance gameplay.

📜 License

This project is released under the MIT License, so feel free to use, modify, and share it with others. Just remember to include a copy of the license if you distribute it.

Happy guessing, and may the odds be ever in your favor! 🎉
