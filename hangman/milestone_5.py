#class definition
import random

class Hangman:

    #class constructor
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(self.word)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower() # Convert guess to lower case
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word): # Enumerate creates an indexed list from arg i == index of letter, letter == letter
                if letter == guess:
                    self.word_guessed[i] = guess # Uses index taken from enumerate
                    self.num_letters = self.num_letters - 1 # reduces number of letters by 1
            print(f'There are {self.num_letters} letters remaining in the word.')
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives - 1 # Reduces number of lives by 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} left") 


    def ask_for_input(self):
        while True:
            guess = input(f"Please input a single letter. ") 
            # asks user for a single letter and assigns it to the variable guess.
            #validate input: single alphabetical character, not already guessed
            if len(guess) != 1 or guess.isalpha() == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: #check if guess is in list_of_guesses
                print(f"You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess) #adds guess to list
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f'You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print(f'Congratulations! You won the game!')
            break

play_game(['keith', 'robbie', 'matthew', 'patrick', 'joanne'])