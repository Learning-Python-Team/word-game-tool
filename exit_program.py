import sys


def exit_program(word):
    # Asks user if they really want to quit the tool
    validate = input('Are you sure you want to exit the tool (Y)es/(N)o: ')

    # Make sure they enter a valid response to the question, if not, keep asking
    while validate.upper() != 'Y' and validate.upper() != 'N':
        print('\nSorry, that was invalid')
        validate = input('Please try again. Would you like to exit the tool: ')

    # If they enter 'y' or 'Y', tool closes
    if validate.upper() == 'Y':
        print('You have exited the tool. Thanks!\n')
        sys.exit()
    # If they enter 'n' or 'N', goes back to tool
    else:
        print('Alright, back to the tool we go.\n')
        return False
