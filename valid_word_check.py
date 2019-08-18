import re


def valid_word_check(user_input):
    # open the .txt file of official scrabble words from 2015 using the 'read' status
    base_word_text_file = open("Collins Scrabble Words (2015).txt", "r")
    # check file mode is read > convert each text file row to a list item
    # split on new lines to separate the row text > read the text > add to base_word_list
    if base_word_text_file.mode == 'r':
        base_word_list = base_word_text_file.read().split('\n')
        base_word_text_file.close()

        # if there are no * tiles, check if input is a valid word
        if '*' not in user_input:
            if user_input in base_word_list:
                return True
        # if there are any * characters in user input:
        elif '*' in user_input:
            # replace all * characters with '[A-Z]'
            pattern = '[A-Z]'.join(user_input.split('*'))
            # then search through the word list using regex
            for item in base_word_list:
                if re.search(pattern, item):
                    return True
        # word not spelt correctly
        else:
            return False
