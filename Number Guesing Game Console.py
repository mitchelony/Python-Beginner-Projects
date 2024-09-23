import random

def number_guessing_game():
    #Welcome Message
    print("\nWelcome To The Number Guessing Game! \nI\'m Thinking Of A Number Between 1 And 10.\n")
    print("Choose Your Difficulty Level: \n1. Easy (10 Attempts) \n2. Medium (5 Attempts) \n3. Hard (3 Attempts)\n")
    
    #Difficulty Setting
    difficulty = int(input("Enter Your Choice (1,2,or 3): "))
    if difficulty == 1:
        attempts = 10
        print("\nBoo! You have Selected Easy Difficulty...\nYou Have 10 Attempts To Guess The Number.\n Let\'s Start The Game!\n")
    elif difficulty == 2:
        attempts = 5
        print("\nOkay! You have Selected Medium Difficulty...\nYou Have 5 Attempts To Guess The Number.\n Let\'s Start The Game!\n")
    elif difficulty == 3:
        attempts = 3
        print("\n Wow! You have Selected Hard Difficulty...\nYou Have 3 Attempts To Guess The Number.\n Let\'s Start The Game!\n")
    else:
        input("Invalid Choice! Press Enter To Try Again.")
    
    #Random Number Generation
    secret_number = random.randint(1,10)

    #Game Loop
    while True:
        guess = int(input("Enter Your Guess: "))
        if guess == secret_number:
            print("Congratulations! You Got It Right! The Number Was " + str(secret_number) + ".")
            print("You Got It In " + str(attempts) + " Attempts.")
            break
        else:
            attempts -= 1
            if guess > secret_number:
                print("Too High! Try Lower.")
            elif guess < secret_number:
                print("Too Low! Try Higher.")
            if attempts == 0:
                print("Game Over! The Number Was " + str(secret_number) + ".")
                break
            print("You Have " + str(attempts) + " Attempts Left!")
number_guessing_game()