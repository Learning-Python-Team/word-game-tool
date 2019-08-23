# main file for program operations
# please make any improvements that could be made!

# import regex library and other file functions
import re
from score_calculator import base_score
from exit_program import exit_program as ep
from word_validation import valid_word_check

print('Welcome to the Word Game Tool!\n')

# Explain purpose of tool to user
print('''This tool allows you to enter a word and receive the word\'s score based on a standardized point 
value system. To use the tool, simply enter the word below, or input \'Q\' to quit.
You may use '*' to represent any letter, but it won't score you any points! \n''')

while True:

    # Gets user input
    user_input = input('Enter the word you want to score: ').upper()

    # if user entered q, validates that they want to exit program
    if user_input == 'Q':
        # if it was entered by accident, it returns to tool
        if ep(user_input) is False:
            continue

    # check for empty input
    elif user_input == '':
        print('You need to enter a word to use the tool!\n')

    # check for valid input - anything other than A - Z or * will be rejected
    elif re.search('[^A-Z*]', user_input):
        print(
            f'You entered {user_input}, which contains characters not found in the alphabet! Stick to A-Z or * please .\n')

    # check for valid word
    elif not valid_word_check(user_input):
        print(f'Sorry, {user_input} may be spelled incorrectly. Try again.\n')

    # process user_input once all checks are cleared
    else:
        user_input_score = base_score(user_input)
        print(f'You entered {user_input}, which scores {user_input_score}\n')
