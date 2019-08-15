# the main functionality of this file is:
#I/O:
#this file will take inputs as 
#in the first line, number of letters to be considered
#in the second line, all the letters, space separated

#functionality:
#we will take that input, create all possible strings using create_stringlist function
#from all possible strings, using nltk, we will keep those which are real words

#return type:
#those words will be returned as a list

#this will become a dependency of our program, it will need nltk, but that is ok for a word based program

from nltk.corpus import words

#take the inputs as mentioned above
number_of_letters=int(input)
letters_as_string=input()
letters_as_list=[letter for letter in letters_as_string.split(" ")]

#function to create all possible strings
def create_stringlist(letter_list):
    #within allowable time-complexity, create all possible strings
    #that action is required to create the list of all possible letters
    return words_list
    

words_from_letters=create_stringlist(letters_as_list)
def words_possible_provider(words_from_letter):
    words_possible=[]
    for word_anagramed in words_from_letters:
        if word_anagramed in words.words():
            words_possible.append(word_anagramed)
    return words_possible
words_possible=words_possible_provider(words_from_letter)
print(words_possible)


