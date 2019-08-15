# main file for program operations
# it's just waiting for you to edit it!!

# Welcome user
print('Welcome to the Word Game Tool!')

from word_to_score import point_conversion

print('This tool allows you to enter a word and receive the word\'s score based on a standardized point value system. To use the tool, simply enter the word below, or enter EXIT_TOOL to quit.')

TOOL_STATUS = 1

while TOOL_STATUS:
    user_input = input('Enter the word you want to score: ')
    if user_input == 'EXIT_TOOL':
        print('You have exited the tool. Thanks!')
        TOOL_STATUS = 0
    else:
        user_input_score = point_conversion(user_input)
        print(f'You entered {user_input}, which scores {user_input_score}')
