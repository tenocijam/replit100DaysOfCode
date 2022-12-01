# Day 39

import random
print()
print("\033[35mHangman Game\033[0m")
print()

word_list = ["british", "suave", "integrity", "accent", "evil", "genius", "downton"]

random_word = random.choice(word_list) # random word choosen from the word_list

user_letters = [] # list of all the correctly entered letters by user
user_word = "" # the word that user has guessed
lives = 6 # lives remaining for the user
game_over = False # variable to check if game is over

while True:
    print()
    letter = input("Type in a letter: ")
    
    # Checks if the user entered letter is in the randomly chosen word
    if letter in random_word:
        print("Correct!")
        user_letters.append(letter) # adds the letter to the list containing correctly entered letters by user
        
        for i in random_word:
            if i in user_letters:
                user_word += i
            else:
                user_word += "_"         
        # Loop to print correctly chosen letters with green color                
        for l in user_word:
            if l != "_":
                print("\033[32m" + l + "\033[0m", end="")
            else:
                print(l, end="")
        
        print()
    else:
        # Decreases user life if the user chooses letter which is not in the randomly chosen word
        print("Incorrect. Try again.")
        lives -= 1
        
    # Prints a message and exits the game if the user guesses the word correctly
    if user_word == random_word:
        print("\n👏 \033[34mCongratulations! You won the game with", lives, "lives left.\033[34m")
        break
        
    # Prints a message and exits the game if the lives of user comes below 1
    if lives < 1:
        print("\n\033[31m😞 Oops! You ran out of lives and lost the game. Try again later.\033[31m")
        break
        
    # Resets user_word to empty string
    user_word = ""