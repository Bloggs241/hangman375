import random

word_list = ['apple', 'banana', 'pineapple', 'kiwi', 'grape'] # a list of my 5 favourite fruits.

word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")    
        guess = input(f"Please input a single letter. ") # asks user for a single letter and assigns it to the variable guess.

def ask_for_input():
    while True:
        guess = input(f"Please input a single letter. ") # asks user for a single letter and assigns it to the variable guess.
        if len(guess) == 1 and guess.isalpha() == True: #check if the guess is a single alphabetical character
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_input()