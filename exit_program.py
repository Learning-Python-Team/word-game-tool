import sys


def exit_program(word):
    # Asks user if they really want to quit the tool
    validate = input('Are you sure you want to exit the tool (Y)es/(N)o: ').upper()

    # Make sure they enter a valid response to the question, if not, keep asking
    while validate != 'Y' and validate != 'N':
        print('\nSorry, that was invalid')
        validate = input('Please try again. Would you like to exit the tool (Y)es/(N)o: ').upper()

    # If they enter 'y', tool closes
    if validate == 'Y':
        print('You have exited the tool. Thanks!\n')
        sys.exit()
    # If they enter 'n', goes back to tool
    else:
        print('Alright, back to the tool we go.\n')
        return False
