
# main file for program operations
# please make any improvements that could be made!

# import regex library for input validation
import re
# import function from word_to_score.py to convert a given word to a point value
from word_to_score import point_conversion
import checkstringer
from checkstringer import check_diff_characters

# Welcome user
print('Welcome to the Word Game Tool!\n')


# Explain purpose of tool to user
print('This tool allows you to enter a word and receive the word\'s score based on a standardized point value system. To use the tool, simply enter the word below, or enter EXIT_TOOL to quit.\n')

# Set tool status constant. 1 is on, 0 is off.
TOOL_STATUS = 1

# while the tool status is on, ask for user input and run function
while TOOL_STATUS:
    user_input = input('Enter the word you want to score: ')
    user_input=user_input.upper()
# if statement to allow user to close the tool
    if user_input == 'EXIT_TOOL':
        print('You have exited the tool. Thanks!\n')
        TOOL_STATUS = 0

# elif statement for empty input:
    elif user_input == '':
        print('You need to enter a word to use the tool!\n')

# elif statement for input validation
    elif check_diff_characters(user_input):
        print(f'You entered {user_input}, which contains characters not found in the alphabet! Stick to A-Z please.\n')

# main function to process correct user input
    else:
        user_input_score = point_conversion(user_input)
        print(f'You entered {user_input}, which scores {user_input_score}\n')
