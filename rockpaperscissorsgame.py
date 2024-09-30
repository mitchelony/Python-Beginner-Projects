import random

def rockpaperscissors_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    player_move = input("Please enter your move. [rock, paper, or scissors]")
    
    while (player_move != "rock") and (player_move != "paper") and (player_move != "scissors"):
        print("Invalid entry! Please try again.")
        player_move = input("Please enter your move. [rock, paper, or scissors]")
    
    print("The player chose: " + player_move)
    
    comp_move = random.randint(1,3)
    if comp_move == 1:
        comp_move = "rock"
    elif comp_move == 2:
        comp_move = "paper"
    else:
        comp_move = "scissors"
    print("The computer chose: " + comp_move)

    outcome = 0
    while outcome == 0:
        if player_move == comp_move:
            print("It's a tie!")
        elif (player_move == 'rock') and (comp_move == 'scissors'):
            print("Player wins!")
            outcome = 1
        elif (player_move == 'rock') and (comp_move == 'paper'):
            print("Computer wins!")
            outcome = 1
        elif (player_move == 'paper') and (comp_move == 'rock'):
            print("Player wins!")
            outcome = 1
        elif (player_move == 'paper') and (comp_move == 'scissors'):
            print("Computer wins!")
            outcome = 1
        elif (player_move == 'scissors') and (comp_move == 'paper'):
            print("Player wins!")
            outcome = 1
        elif (player_move == 'scissors') and (comp_move == 'rock'):
            print("Computer wins!")
            outcome = 1

rockpaperscissors_game()
