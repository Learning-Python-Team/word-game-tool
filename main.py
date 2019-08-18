# main file for program operations
# please make any improvements that could be made!

# import regex library and other file functions
import re
from word_to_score import point_conversion
from valid_word_check import valid_word_check

print('Welcome to the Word Game Tool!\n')

# Explain purpose of tool to user
print('''This tool allows you to enter a word and receive the word\'s score based on a standardized point 
value system. To use the tool, simply enter the word below.
You may use '*' to represent any letter, but it won't score you any points! Enter EXIT_TOOL to quit.\n''')

# Boolean check for while loop. 1 is true (on), 0 is false (off).
TOOL_STATUS = 1

# while the tool status is on, ask for user input and run function
while TOOL_STATUS:
    user_input = input('Enter the word you want to score: ').upper()

    # allow user to close the tool
    if user_input == 'EXIT_TOOL':
        print('You have exited the tool. Thanks!\n')
        TOOL_STATUS = 0

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
        user_input_score = point_conversion(user_input)
        print(f'You entered {user_input}, which scores {user_input_score}\n')
