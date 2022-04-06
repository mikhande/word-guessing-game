#Game
our_word = 'onomatopoeia'

#word = str and len > 1

#letter = str and len == 1

player_guess_num = 7

player_guesses = []

length = len(our_word)

show_word = '_' * length

def lose_turn():
    player_guess_num = player_guess_num - 1

def run_guess():
    player_guess = False
    while player_guess == False and player_guess_num > 0:
        guess = input('Guess a letter or a word: ')
        if guess.isalpha():
            if len(guess) > 1: #This is the condition if it's a word
                if guess == our_word: #The person guesses word correctly
                    print('Congratulations, you win!')
                elif guess != our_word: #person guesses word incorrectly, loses turn, and guesses again.
                    print("Sorry, that's not it. Try again.")
                    lose_turn
                    run_guess
                print(len(guess)) 
            elif len(guess) == 1: #This is the condition if it's a letter
                print
        else:
            print("That is not a letter or a word... try again.")
            run_guess()

run_guess()

