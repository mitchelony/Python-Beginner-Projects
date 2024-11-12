***Mitchel’s Python Wordle 🎉***

Welcome to Mitchel’s Python Wordle, where guessing words isn’t just a pastime—it’s a challenge! This version of Wordle is coded entirely in Python, using color-coded hints to guide you towards the winning word. Do you have what it takes to solve the puzzle within six tries?

🎮 How the Game Works

In each game, you’re faced with a five-letter mystery word. The goal? Guess the word within six attempts. After each guess, the game will provide feedback in the form of color-coded letters. Each color reveals how close you are:

	•	Green 🟩 means the letter is in the word and in the correct position.
	•	Yellow 🟨 means the letter is in the word but in the wrong position.
	•	Red 🟥 means the letter isn’t in the word at all.

With each guess, the game helps you narrow down possibilities, rewarding both luck and strategy!

⚙️ Game Logic & Design

This Wordle game is built around a simple yet effective feedback loop and color-coded guidance to keep gameplay intuitive. Here’s the main logic flow:

	1.	Random Word Selection:
	•	A word is randomly chosen from an external text file (word.txt). For testing purposes, you can also pass a specific word via the command line, making it easy to test without waiting for luck to land on the word you want.
	2.	User Input & Validation:
	•	Players are prompted to guess a five-letter word.
	•	Input validation ensures guesses are always five letters long, giving players instant feedback if they go off-track.
	3.	Letter Comparison:
	•	The guessed word is compared against the answer, letter by letter.
	•	Each letter receives color-coded feedback:
	•	Green if the letter is correct and in the right position.
	•	Yellow if the letter is correct but in the wrong position.
	•	Red if the letter doesn’t appear in the word.
	•	This feedback is presented after each guess, helping players refine their guesses as they progress.
	4.	End Conditions:
	•	The game ends if the player either guesses the word correctly (congratulations!) or runs out of attempts (better luck next time!).
	•	If the player wins, they receive a fun congratulatory message. If not, they can always play again with a new word!

🛠 Running the Game

To play the game, you’ll need Python 3 installed on your system.

Steps:

	1.	Clone or download this project to your computer.
	2.	Open a terminal and navigate to the directory containing wordle.py.
	3.	Run the game with:

python wordle.py


	4.	(Optional) For testing purposes, you can specify a word directly:

python wordle.py apple



🔧 Customizations and Expansions

The current code offers easy opportunities to expand or personalize:

	•	Custom Word Lists: You can edit word.txt to add your favorite five-letter words or make a themed Wordle game!
	•	Difficulty Levels: Try increasing or decreasing the number of guesses to change the difficulty.
	•	Color Codes: If you’re feeling fancy, adjust the colors to fit your theme or add even more playful feedback.

📜 License

This project is licensed under the MIT License, which means you’re free to use, modify, and distribute this code as long as you include a copy of the license in any substantial portions of the software. Enjoy building and sharing your own versions of this Wordle game!

Happy guessing! 🎉
