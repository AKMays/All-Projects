"""
Purpose: Replicate the game hangman
Authors: Adonte Mays
Date: 11/14/2022
Updated: 12/25/2022
"""
import string

def hangman(word, filled_word, guesses, letters):
    if not(isinstance(word, str)):
        print("Word must be a string!")
        return 0
    elif not(isinstance(filled_word, str)):
        print("filled_word must be a string!")
        return 0
    elif not(isinstance(guesses, int)):
        print("guesses must be an integer!")
        return 0
    elif word == filled_word:
        print("Congratulations, you won!")
        return 1
    elif guesses < 1:
        return 0
    print("Welcome to hangman!")
    print("I am thinking of a word that is", len(word), "letters long... ")
    print("You have", guesses, "guesses remaining")
    for char in word:
        filled_word = len(word) * "-"
    letters = string.ascii_lowercase

    while guesses > 0:
        print("Available letters:", letters)
        letter = input("Please guess a letter: ").lower()
        if len(letter) != 1 or letter not in letters:
            print("Invalid input. Please enter a single letter that you haven't guessed yet.")
            continue
        if letter in word:
            new_filled_word = []
            for i, char in enumerate(word):
                if char == letter:
                    new_filled_word.append(letter)
                else:
                    new_filled_word.append(filled_word[i])
            filled_word = "".join(new_filled_word)
            print("Great guess! Current word:", filled_word)
            if filled_word == word:
                print("Congratulations, you won!")
                return 1
        else:
            print("Oops! That letter is not in my word:", filled_word)
            guesses -= 1
        letters = letters.replace(letter, "")

    print("Sorry, you ran out of guesses. The word was", word + ".")
    return 0

hangman("Denison", "", 10, string.ascii_lowercase)

# email - mays_a1@denison.edu
