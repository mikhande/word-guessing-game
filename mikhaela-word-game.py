#Game
our_word = 'onomatopoeia'

word = str and len > 1

letter = str and len == 1

player_guess_num = 7

show_word = ""
for x in len(our_word):
    show_word +='_'

player_guesses =[]

length = len(our_word)

player_guess = False
while player_guess == False:
    guess = str(input('Guess a letter or a word: '))
    if guess != str:
        print('That is not a word or a letter... try again.')
