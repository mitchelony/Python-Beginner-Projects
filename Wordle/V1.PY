def wordle():
    # Section 1: Imports and Game Setup
    import random  # For generating a random word from the dictionary
    
    # List of potential words for the game
    word_dict = ["apple", "brave", "crane", "doubt", "eagle",
                 "flame", "grape", "house", "input", "jolly",
                 "knock", "lemon", "mango", "noble", "ocean",
                 "pride", "quilt", "raven", "stone", "tiger"]
    
    # Define text colors for correct (green), partially correct (yellow), and incorrect (red) guesses
    class bcolors:
        YELLOW = '\033[0;33;40m'
        GREEN = '\033[0;32;40m'
        RED = '\033[0;31;40m'

    # Randomly select a word from the dictionary
    answer = random.choice(word_dict)
    answer_list = list(answer)  # Convert selected word to a list of characters for easy comparison
    
    # Initialize game variables
    tries = 6        # Number of attempts allowed
    game_end = False # Game loop control flag

    # Section 2: Game Introduction
    print('\033[0;37;40mWelcome To Mitchel\'s Wordle!')
    username = input('\033[0;37;40mWhat\'s Your Name, Great Adventurer? ')
    print(f'\033[0;37;40mHAHA! That\'s A Great Name Sir {username}\nIt\'s Time To Play!')

    # Section 3: Game Loop
    while not game_end:
        # Prompt the user for their guess and validate it
        user_choice = input('\033[0;37;40mEnter Your Guess? (Must Be A 5-Letter Word): ')
        
        # Check if the guess is exactly 5 letters long
        if len(user_choice) != 5:
            print('\033[0;37;40mERROR! This is not a 5-letter word. Please enter a five-letter word.')
            continue

        # Reduce remaining tries and convert user choice to a list of characters
        tries -= 1
        user_list = list(user_choice)
        
        # Check if out of attempts
        if tries <= 0:
            game_end = True
        
        # Section 4: Letter Comparison and Feedback
        result = [''] * 5  # Reset the result list for the current guess
        
        # Compare each letter of the user's guess with the answer
        for i in range(5):
            if answer_list[i] == user_list[i]:
                # Exact match - Green
                result[i] = (bcolors.GREEN + f' {user_list[i]} - Green')
            elif user_list[i] in answer_list:
                # Letter in the word but wrong position - Yellow
                result[i] = (bcolors.YELLOW + f' {user_list[i]} - Yellow')
            else:
                # Letter not in the word - Red
                result[i] = (bcolors.RED + f' {user_list[i]} - Red')
        
        # Print feedback for each letter in the guess
        for feedback in result:
            print(feedback)

        # Check for a win condition
        if answer == user_choice:
            print(f'You Won, Sir {username}!')
            game_end = True

# Run the game
wordle()