def wordle():
    import random
    # word_dict = ["apple", "brave", "crane", "doubt", "eagle",
    #              "flame", "grape", "house", "input", "jolly",
    #              "knock", "lemon", "mango", "noble", "ocean",
    #              "pride", "quilt", "raven", "stone", "tiger"]
    word_dict = ['apple']
    class bcolors:
        YELLOW = '\033[0;33;40m'
        GREEN = '\033[0;32;40m'
        RED = '\033[0;31;40m'
    answer = random.choice(word_dict)
    answer_list = [answer[0], answer[1], answer[2], answer[3], answer[4]]
    tries = 6
    game_end = False
    print('\033[0;37;40mWelcome To Mitchel\'s Wordle!')
    username = input('\033[0;37;40mWhat\'s Your Name Great Adventurer? ')
    print(f'\033[0;37;40mHAHA! That\'s A Great Name Sir {username}\nIts Time To Play!')
    user_list = []
    result = ['', '', '', '', '']
    while not game_end:
        user_choice = input('\033[0;37;40mEnter Your Guess? (Must Be A 5-Letter Word): ')
        if len(user_choice) != 5:
            print('\033[0;37;40mERROR! This is not a 5 letter Word. Please Enter A Five Letter Word.')
            continue
        tries -= 1
        user_list = [user_choice[0], user_choice[1], user_choice[2], user_choice[3], user_choice[4]]
        if tries <= 0:
            game_end = True   
        for i in range(0,5):
            if answer_list[i] == user_list[i]:
                result[i] = (bcolors.GREEN + f' {user_list[i]} - Green')
            elif user_list[i] in answer_list:
                result[i] = (bcolors.YELLOW + f' {user_list[i]} - Yellow')
            else:
                result[i] = (bcolors.RED + f' {user_list[i]} - Red')
        for j in result:
            print(j)
        if answer == user_choice:
            print(f'You Won Sir {username}!')
            game_end = True
wordle()

