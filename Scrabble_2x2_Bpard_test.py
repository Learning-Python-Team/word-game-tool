

# Values of individual alphabet tiles

tiles_points = {'c': 3, ' d': 2}


# Quantity of individual alphabet tiles. Probably wont be used.

tiles_qty = {'a': 9, 'b': 2}


# Simple 2x2 board
# Keys - Columns alphabet (a,b) and rows are numbers (1,2)
# e.g. a1, b2
# Values: board position values
# e.g. dw = double word score, tl = triple letter score

dict_board = {'a1': 'dw', 'a2': 'dw', 'b1': 'tl', 'b2': 'tl'}
list_board_dw = ['a1', 'a2']
list_board_tl = ['b1', 'b2']


# For testing - valid input is ab or ba

word = str(input())


# Location of first letter in word. input(board.key)
# For testing valid input is keys from dict_board = a1, a2, b1, b2

word_start = str(input())



# This tests if input for word_start is a valid board location.
if word_start not in list(board.keys()):
    print('Sorry, invalid input. Try again? Yes or No')
else:
    print('Thank you. Valid input')


# Converts the input word to a list object
word_list = list(word)


# Need to iterate through the letters of the word
# then get corresponding values from tiles_points variable
# Then use the points and multiply by the location value on the board (e.g. Double word score)

for letter in word_list:
    if letter in tiles_points.keys():
        print(tiles_points.get(letter))


# define function to convert a word to the point value of its' tiles
def point_conversion(word):
    # dictionary of letters and their point values
    tile_value_dict = {
        ' ': 0,
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10,
    }
    score = 0
    for char in word:
        score += tile_value_dict[char]
    return score
