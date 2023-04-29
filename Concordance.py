"""
@author John Droder, Adonte Mays
@description Class Project #1
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
#End of code due to this being a school project(if you'd like the entire file let me know! email - mays_a1@denison.edu).
