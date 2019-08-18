# main file for program operations
# please make any improvements that could be made!

# import regex library for input validation
import re
# import function from word_to_score.py to convert a given word to a point value
from word_to_score import point_conversion
# import exit program to check if user wants to exit tool
from exit_program import exit_program as ep

# Welcome user
print('Welcome to the Word Game Tool!\n')


# Explain purpose of tool to user
print('This tool allows you to enter a word and receive the word\'s score based on a standardized point value system. To use the tool, simply enter the word below, or input \'Q\' to quit.\n')

while True:

    # Gets user input
    user_input = input('Enter the word you want to score: ').upper()

    # if user entered q, validates that they want to exit program
    if user_input == 'Q':
        # if it was entered by accident, it returns to tool
        if ep(user_input) is False:
            continue

    # if statement for empty input:
    elif user_input == '':
        print('You need to enter a word to use the tool!\n')

    # elif statement for input validation
    elif re.search('[\d\W]', user_input):
        print(f'You entered {user_input}, which contains characters not found in the alphabet! Stick to A-Z please.\n')

    # main function to process correct user input
    else:
        user_input_score = point_conversion(user_input)
        print(f'You entered {user_input}, which scores {user_input_score}\n')
