#Game
import random

file_path = (r'exercises\week 5 - python basics\word-guessing-game\words.txt')

def random_word(fname):
    word_dictionary = open("words.txt")
    our_word = random.choice(word_dictionary.read().split())
    word_dictionary.close()
    return our_word

our_word = random_word('words.txt')

our_word_list = list(our_word)

wins = 0 # Can't get wins and losses to add a point.. 
losses = 0

def win():
    if player_guess == True:
        wins += 1

def loss():
    if player_guess == False:
        losses += 1

correct_letters = []

for char in our_word: # for the character in the word, it will change the blank spaces to include the new guessed letter
        correct_letters.append("_")

player_guess = False

def wins_losses():
    print("You have won: " + str(wins) + " games and have lost: " + str(losses) + " games.")

def play_again():
    response = input("Do you want to play again? y = yes, n = no: ")
    if response == 'y':
        run_guess()
    else: 
        print('Thanks for playing!')

# def add_point(): #this isn't working
#     if player_guess == True:
#         win + 1
#     else:
#         loss + 1

def run_guess():
    # our_word = 'onomatopoeia'

    # correct_letters = []

    our_word_list = list(our_word)

    player_guess_num = 7

    player_guesses = []

    # wins = 0

    # losses = 0

    for char in our_word: # for the character in the word, it will change the blank spaces to include the new guessed letter
        correct_letters.append("_")
    player_guess = False

    while player_guess == False and player_guess_num > 0:
        print("You have " + str(player_guess_num) + " guesses")
        guess = input('Guess a letter or a word: ')  
        for position in range(len(our_word_list)):
            if our_word_list[position] == guess:
                correct_letters[position] = guess

        if guess.isalpha():
            if len(guess) > 1: #This is the condition if it's a word
                if guess == our_word: #The person guesses word correctly - this part works!
                    print('Congratulations, you win!')
                    player_guess = True
                    win()
                    # wins += 1
                    wins_losses()
                    play_again()
                elif guess in player_guesses: 
                    print('You have already guessed ' + str(guess).upper() + ' here are your previous guesses: ' + str(player_guesses))#working
                elif guess != our_word: #person guesses word incorrectly, loses turn, and guesses again. 
                    print("Sorry, that's not it.")
                    player_guesses.append(guess)
                    player_guess_num -= 1 #This is working

            elif len(guess) == 1: #This is the condition if it's a letter
                if guess in our_word and '_' in correct_letters: #This is if you have guessed a letter in the word but haven't guessed the full word
                    print('That letter is in the word!')
                    player_guesses.append(guess)
                    print(correct_letters) #This prints the correct letter inserted into the blank spaces of the word
                elif '_' not in correct_letters: #This is if you have guessed the full word by guessing letters 
                    print("Congratulations, the word was " + our_word + ". You win!")
                    player_guess = True 
                    win()
                    # wins += 1 #this isn't working
                    play_again()
                elif guess in player_guesses:
                    print('Sorry, you have already guessed that. Here are your previous guesses: ' + str(player_guesses)) #working
                elif guess != our_word:
                    print('Sorry, that is not in the word.') # This is working
                    player_guesses.append(guess)
                    player_guess_num -= 1

        else: #This is for if the input is not alphanumeric. - this part works!
            print("That is not a letter or a word... try again.")

    if player_guess_num == 0:
        print("Oh, no! You ran out of gueses. The word was " + str(our_word).upper())
        # loss()
        # losses += 1
        wins_losses()
        play_again()
            



run_guess()


