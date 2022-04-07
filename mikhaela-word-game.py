#Game
our_word = 'onomatopoeia'
correct_letters = []



our_word_list = list(our_word)

# for char in our_word:
#     correct_letters.append("_")  
# for position in range(len(our_word_list)):
#     if our_word_list[position] == guess:
#         print(position)
#         print(our_word_list[position])
#         correct_letters[position] = guess


#print(our_word_list)
#print(our_word_letters)

#player_guess_num = 7

#player_guesses = []

#length = len(our_word)

#show_word = '_' * length

def run_guess():
    our_word = 'onomatopoeia'
    correct_letters = []
    our_word_list = list(our_word)
    player_guess_num = 7
    player_guesses = []
    for char in our_word:
        correct_letters.append("_")
    # length = len(our_word)
    # show_word = '_' * length
    player_guess = False
    while player_guess == False and player_guess_num > 0:
        print("You have " + str(player_guess_num) + " guesses")
        guess = input('Guess a letter or a word: ')
        # for char in our_word:
        #     correct_letters.append("_")  
        for position in range(len(our_word_list)):
            if our_word_list[position] == guess:
                # print(position)
                # print(our_word_list[position])
                correct_letters[position] = guess
        if guess.isalpha():
            if len(guess) > 1: #This is the condition if it's a word
                if guess == our_word: #The person guesses word correctly - this part works!
                    print('Congratulations, you win!')
                elif guess in player_guesses: 
                    print('You have already guessed ' + str(guess) + ' Try again.')#working
                elif guess != our_word: #person guesses word incorrectly, loses turn, and guesses again. 
                    print("Sorry, that's not it. Try again.")
                    player_guesses.append(guess)
                    player_guess_num -= 1 #This is working
                #print(len(guess)) 
            elif len(guess) == 1: #This is the condition if it's a letter
                if guess in our_word:
                    print('That letter is in the word!')
                    player_guesses.append(guess)
                    #print(our_word_list)
                    print(correct_letters)
                elif guess in player_guesses:
                    print('Sorry, you have already guessed that.') #working
                elif guess != our_word:
                    print('Sorry, that is not in the word. Try again.') # This is working
                    player_guesses.append(guess)
                    player_guess_num -=1
        else: #This is for if the input is not alphanumeric. - this part works!
            print("That is not a letter or a word... try again.")
            



run_guess()


