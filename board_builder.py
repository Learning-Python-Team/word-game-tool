import numpy as np


def create_board():
    # to build the board we create multiple layers:
    # 1. a user input layer which will be updated later to carry the input word
    # 2. a letter multiplier layer that will be used to calculate the word score
    # 3. a word multiplier layer that will be used to calculate the total word score
    # the layers will be a 15x15 2d numpy array, which will be stacked and returned to the main function

    # define locations of triple and double word tiles (taken from an actual board)
    triple_word_idx = ((0, 0, 0, 7, 7, 14, 14, 14), (0, 7, 14, 0, 14, 0, 7, 14))
    double_word_idx = ((1, 1, 2, 2, 3, 3, 4, 4, 10, 10, 11, 11, 12, 12, 13, 13,7),
                       (1, 13, 2, 12, 3, 11, 4, 10, 4, 10, 3, 11, 2, 12, 1, 13,7))
    # create the word multiplier layer
    word_multiplier_array = np.full((15, 15), 1)
    word_multiplier_array[triple_word_idx] = 3
    word_multiplier_array[double_word_idx] = 2

    # the same is done for the letter multiplier layer
    double_letter_idx = ((0, 0, 2, 2, 3, 3, 3, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 11, 11, 11, 12, 12, 14, 14),
                         (3, 11, 6, 8, 0, 7, 14, 2, 6, 8, 12, 3, 11, 2, 6, 8, 12, 0, 7, 14, 6, 8, 3, 11))
    triple_letter_idx = ((1, 1, 5, 5, 5, 5, 9, 9, 9, 9, 13, 13),
                         (5, 9, 1, 5, 9, 13, 1, 5, 9, 13, 5, 9))
    letter_multiplier_array = np.full((15, 15), 1)
    letter_multiplier_array[double_letter_idx] = 2
    letter_multiplier_array[triple_letter_idx] = 3

    # create the input layer
    input_array = np.full((15, 15), np.nan)

    # finally combine the three layers to a 3d array and return
    return np.stack((input_array, letter_multiplier_array, word_multiplier_array))


def view_board():
    pass
   
