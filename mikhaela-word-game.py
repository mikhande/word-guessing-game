#Game
our_word = 'onomatopoeia'

#word = str and len > 1

#letter = str and len == 1

player_guess_num = 7

player_guesses = []

length = len(our_word)

show_word = '_' * length

def run_guess():
    player_guess = False
    while player_guess == False and player_guess_num > 0:
        guess = input('Guess a letter or a word: ')
        print(type(guess))
        if guess.isalpha():
            if len(guess) > 1:
                print(len(guess)) #This is the condition if it's a word
            elif len(guess) == 1: #This is the condition if it's a letter
                print
        else:
            print("That is not a lett or a word... try again.")
            run_guess()

        
        #if type(guess) != str:
            #print('That is not a word or a letter... try again.')

run_guess()

