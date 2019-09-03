import PySimpleGUI as sg
import re
from word_to_score import point_conversion
from valid_word_check import valid_word_check

layout = [[sg.Text('''This tool allows you to enter a word and receive the word\'s score based on a standardized point 
    value system. To use the tool, simply enter the word below, or input \'Q\' to quit.
    You may use '*' to represent any letter, but it won't score you any points! \n''')],
    [sg.Input()],
    [sg.OK()]]

event, values = sg.Window('Enter a word', layout).Read()

# Gets user input
user_input = values[0].upper()

# check for valid input - anything other than A - Z or * will be rejected
if re.search('[^A-Z*]', user_input):
    print(
        f'You entered {user_input}, which contains characters not found in the alphabet! Stick to A-Z or * please .\n')

# check for valid word
elif not valid_word_check(user_input):
    print(f'Sorry, {user_input} may be spelled incorrectly. Try again.\n')

# process user_input once all checks are cleared
else:
    user_input_score = point_conversion(user_input)
    print(f'You entered {user_input}, which scores {user_input_score}\n')

sg.Popup(f"The score is {user_input_score}", values[0], )
