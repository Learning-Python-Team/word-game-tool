# main file for program operations
# please make any improvements that could be made!

# import regex library for input validation
import re
# import function from word_to_score.py to convert a given word to a point value
from word_to_score import point_conversion

# open the .txt file of official scrabble words from 2015 using the 'read' status
base_word_text_file = open("Collins Scrabble Words (2015).txt", "r")
# check to make sure the file mode is read, then take each row from the text file and make it a list item
# using split on new lines to separate the text on each row, read the text, then add it to the base_word_list list
if base_word_text_file.mode == 'r':
    base_word_list = base_word_text_file.read().split('\n')
    base_word_text_file.close()

# Welcome user
print('Welcome to the Word Game Tool!\n')


# Explain purpose of tool to user
print('''This tool allows you to enter a word and receive the word\'s score based on a standardized point 
value system. To use the tool, simply enter the word below, or enter EXIT_TOOL to quit.\n''')

# Set tool status constant. 1 is on, 0 is off.
TOOL_STATUS = 1

# while the tool status is on, ask for user input and run function
while TOOL_STATUS:
    user_input = input('Enter the word you want to score: ').upper()

# if statement to allow user to close the tool
    if user_input == 'EXIT_TOOL':
        print('You have exited the tool. Thanks!\n')
        TOOL_STATUS = 0

# elif statement for empty input:
    elif user_input == '':
        print('You need to enter a word to use the tool!\n')

# elif statement for input validation
    elif re.search('[^a-zA-Z]', user_input):
        print(f'You entered {user_input}, which contains characters not found in the alphabet! Stick to A-Z please.\n')

# elif statement to validate that input is a correctly spelled English word
    # We use the base_word_list created from our .txt file
    elif user_input not in base_word_list:
        print(f'Sorry, {user_input} may be spelled incorrectly. Try again.')

# main function to process correct user input
    else:
        user_input_score = point_conversion(user_input)
        print(f'You entered {user_input}, which scores {user_input_score}\n')
