"""
@author John Droder, Adonte Mays
@description Project #1 for CS173
@date 2023/1/20
@updated 2023/1/20
"""
# Function needed to keep a list of all words (converted to lowercase), and keeps a list of where a word appears in each sentence.
def sortThroughText(input_txt):

    # Part 1 - Sort the words alphabetically:
    words = input_txt.split() # splits each of the words, defaults to split on every whitespace character, puts each split word into list.
    new_words = [] # creates a new list called new_words
    for word in words: # for-loop to iterate through each word in the split words list, 'words', above
        new_word = word.lower() # makes current word in the for-loop become lower-case, assigned to new_word
        if "." in new_word: # if there is a period in the current word, replace it with nothing
            new_word = new_word.replace(".","") # replaces period with nothing
        new_words.append(new_word) # appends the now lower-case word, without a period, to the new_words list
    unique_words = set(new_words) # set makes sure each value in our list is distinct - so for example... no repeats of the word 'jane'
    unique_words = list(unique_words) # converts the altered set-type back into a list now that we have our distinct values
    unique_words.sort() # sorts the list of unique words alphabetically
    for word in unique_words: # goes through each word, and prints it out
        print(word) # prints current word in for-loop

    # Part 2 - find where the words appear:
    print("Enter a word: ") # question that prompts the user to enter a search query for a word 
    user_input = input() # gets the input from the user
    splitted_sentence = input_txt.strip().split(".") # strips (removes white space), and splits on a period, so we have only the sentences
    if user_input.lower() not in unique_words: # if the user input (in lower case) is not in the unique words list, the word given is not in the original text. 
        print("That word is not located in any sentence.") # prints it to inform the user that the word is non-existant in the text.
    else: # otherwise...
        print(user_input + " appears in:") # informs the user that something is found, and it is now searching...
        for sentence in splitted_sentence: # for loop to find out where the word is found in the sentences
            if user_input.lower() in sentence.lower(): # if the user input is in the sentence...
                print(str(splitted_sentence.index(sentence)+1) + ": " + sentence) # print the index (plus 1) of the sentence, and then print the sentence.

    
file = open("input.txt", "r") # tells python to open the input.txt file as type 'r', meaning we don't need to write to it, only read it.
input_text = file.read() # python reads the file, stores it in input_text
sortThroughText(input_text) # calls the function above on the read python file
file.close() # closes the file when it is done
