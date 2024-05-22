import random

word_list = ['apple', 'banana', 'pineapple', 'kiwi', 'grape'] # a list of my 5 favourite fruits.

#print(word_list)

word = random.choice(word_list) # chooses a random item from the list and assigns it to the variable word.

#print(word)

guess = input(f"Please input a single letter. ") # asks user for a single letter and assigns it to the variable guess.

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input!")