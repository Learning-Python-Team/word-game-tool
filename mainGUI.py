import PySimpleGUI as sg
import re
from word_to_score import point_conversion
from valid_word_check import valid_word_check

layout = [[sg.Text('''This tool allows you to enter a word and receive the word\'s score based on a standardized point 
value system. To use the tool, simply enter the word below, \n
You may use '*' to represent any letter, but it won't score you any points! \n'''),
           sg.Text('', size=(15, 1), key='_OUTPUT_')],
          [sg.Input(key='_IN_', do_not_clear=False)],
          [sg.Button('Score'), sg.Button('Exit')]]

window = sg.Window('Scrabble Points Finder', layout)

while True:  # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    user_input = values['_IN_'].upper()
    if event == 'Score':
        # check for empty input
        if user_input == '':
            sg.Popup('You need to enter a word to use the tool!\n')

        # check for valid input - anything other than A - Z or * will be rejected
        elif re.search('[^A-Z*]', user_input):
            sg.Popup(f'You entered {user_input}, which contains characters not found in the alphabet!\n')

        # check for valid word
        elif not valid_word_check(user_input):
            sg.Popup(f'Sorry, {user_input} may be spelled incorrectly. Try again.\n')

        # process user_input once all checks are cleared
        else:
            user_input_score = point_conversion(user_input)
            print(f'You entered {user_input}, which scores {user_input_score}\n')
            # Update the "output" element to be the value of "input" element
            window.Element('_OUTPUT_').Update(values['_IN_']), user_input_score
            sg.Popup(f"The score is {user_input_score}", values['_IN_'], )

window.Close()
