from multiprocessing.connection import answer_challenge
import random  # For generating a random word from the dictionary
import sys

def get_random_word():
    """
    This function selects a random word either from the command-line argument 
    or from a file called 'word.txt'. If a word is provided via the command-line, 
    it uses that word for testing purposes.
    """
    if len(sys.argv) > 1:
        return sys.argv[1]  # Return the word passed as a command-line argument
    else:
        # Open the file containing the list of words and choose a random one
        with open("Python-Beginner-Projects/Wordle/word.txt", "r") as file:
            words = [word.strip() for word in file.readlines()]  # Read the words from the file and remove newlines
            return random.choice(words)  # Randomly choose one word from the list

class bcolors:
    """This class defines the color codes used for feedback text in the terminal."""
    YELLOW = '\033[0;33m'  # Yellow text for partially correct letters
    GREEN = '\033[0;32m'   # Green text for exact matches
    RED = '\033[0;31m'     # Red text for incorrect letters
    RESET = '\033[0;37m'   # Resets color back to default (white)

def print_intro():
    """
    This function prints the welcome message, prompts the user for their name,
    and introduces the game. It also returns the player's name for later use.
    """
    print(f"{bcolors.RESET}Welcome To Mitchel's Wordle!")
    username = input(f"{bcolors.RESET}What's Your Name, Great Adventurer? ")
    print(f"{bcolors.RESET}HAHA! That's A Great Name Sir {username}\nIt's Time To Play!")
    return username  # Return the username to be used later in the game

def get_user_guess():
    """
    This function repeatedly asks the user for a valid 5-letter word guess.
    It ensures the input is exactly 5 letters long and returns it.
    """
    while True:
        guess = input(f"{bcolors.RESET}Enter Your Guess? (Must Be A 5-Letter Word): ")
        if len(guess) == 5:  # Validate if the guess has exactly 5 letters
            return guess  # Return the valid 5-letter guess
        print(f"{bcolors.RESET}ERROR! This is not a 5-letter word. Please enter a five-letter word.")  # Error message for invalid input

def compare_guess(answer_list, user_list):
    """
    This function compares the user's guess to the correct answer.
    It returns a list of feedback indicating whether each letter is:
    - Green: Correct letter in the correct position
    - Yellow: Correct letter but in the wrong position
    - Red: Incorrect letter not present in the answer
    """
    result = [''] * 5  # Initialize a result list to store the feedback for each letter of the guess
    for i in range(5):
        if answer_list[i] == user_list[i]:
            # Exact match - Color Green
            result[i] = f"{bcolors.GREEN} {user_list[i]} - Green"
        elif user_list[i] in answer_list:
            # Letter is in the word but wrong position - Color Yellow
            result[i] = f"{bcolors.YELLOW} {user_list[i]} - Yellow"
        else:
            # Letter is not in the word - Color Red
            result[i] = f"{bcolors.RED} {user_list[i]} - Red"
    return result  # Return the list of feedback for the user's guess

def print_feedback(result):
    """
    This function prints the feedback for each letter of the user's guess.
    It iterates over the feedback results and prints them with the appropriate color.
    """
    for feedback in result:
        print(feedback)  # Print each feedback line (colored text)
    print(bcolors.RESET)  # Reset color after printing feedback

def wordle():
    """
    Main function to run the Wordle game. This function initializes the game,
    handles the game loop, and processes the guesses.
    """
    # Initialize game setup
    answer = get_random_word()
    print(answer)
    # Get a random word as the answer
    answer_list = list(answer)  # Convert the answer word into a list of characters for easy comparison
    tries = 6  # Maximum number of attempts the player has
    game_end = False  # Flag to control the game loop
    
    # Print introduction and get the username
    username = print_intro()
    
    # Game loop
    while not game_end:
        # Get the user's guess and convert it to a list of characters
        user_choice = get_user_guess()
        user_list = list(user_choice)
        
        # Check if the player's guess matches the answer
        if answer == user_choice:
            print(f"You Won, Sir {username}!")  # Congratulate the user if they win
            game_end = True  # End the game
            continue  # Skip to the end of the loop to avoid further processing
        
        # Reduce the number of tries after each guess
        tries -= 1
        if tries <= 0:
            game_end = True  # End the game if the player runs out of attempts
            print(f"Out of tries! The correct word was '{answer}'. Better luck next time, Sir {username}!")  # Reveal the correct word
            continue  # Skip to the end of the loop since the game is over
        
        # Compare the user's guess to the correct answer and generate feedback
        result = compare_guess(answer_list, user_list)
        print_feedback(result)  # Print the feedback for the current guess

# Run the game
wordle()  # Call the main function to start the game