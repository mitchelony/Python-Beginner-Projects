import random
def number_guessing_game():
    secret_number = 5
    attempts = 0
    while True:
        guess = int(input("Guess A Number Between 1 And 10 "))
        attempts += 1

        if guess == secret_number:
            print("Congratulations! You got it in " + str(attempts) + " attempts!")
            break
        elif guess > secret_number:
            print("Too High! Try Lower.")
        elif guess < secret_number:
            print("Too Low! Try Higher.")
        if attempts >= 5:
            print("Too Many Attempts! The Number was ", secret_number)

number_guessing_game()

