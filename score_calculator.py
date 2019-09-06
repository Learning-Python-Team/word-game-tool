# function to convert a word to the base point value using the letter value

import board_builder
import numpy as np

# global dictionary of (letters, point values)
char_dict = {
	'*': 0,
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


def base_score(word):
	# sums each char score
	return sum([char_dict[char] for char in word])


def letter_multiplier_check(word_dict, word_pos_dict):
	# checks for letter multipliers and calculates new score
	letter_score_matrix = board_builder.letter_score_calc()  # call letter score matrix from board_builder.py

	for key, val in word_pos_dict.items():
		if key in letter_score_matrix:
			word_dict[val] = word_dict[val] * letter_score_matrix[key]
		else:
			continue

	return word_dict, sum(word_dict.values())


def word_multiplier_check(word_pos_dict, score):
	# checks for word multipliers and calculates new score
	word_score_matrix = board_builder.word_score_calc() # call word score matrix from board_builder.py

	for key in word_pos_dict.keys():
		if key in word_score_matrix:
			score *= word_score_matrix[key]

	return score


# create a function to increase the tile based on the length of the word, the direction, and the starting tile
def tile_step(word, position, direction):
	# horizontal step: increase letter
	alphabet = 'ABCDEFGHIZKLMNOPQRSTUVWXYZ'
	if direction == 'horizontal':
		letter = position[0]
		letter = alphabet[int(alphabet.index(letter)) + 1]
		number = position[1]
	# vertical step: increase number
	elif direction == 'vertical':
		letter = position[0]
		number = int(position[1]) + 1
	else:
		print('Direction error: direction is neither vertical nor horizontal.')
	new_position = f'{letter}{number}'
	return new_position


def multiplier_score(word, start_pos, direction):
	# calulates word score including any multiplier tiles

	# take start_pos (starting tile) and direction (indicated by user) and create pos_lst
	pos = [start_pos]
	# build position list based on length of word
	for letter in word[1:]:
		new_tileslot = tile_step(word, pos[len(pos) - 1], direction)
		pos.append(new_tileslot)

	# receive list of word positions
	letter_pos_list = pos  # Ex: pos = ['D8', 'E8', 'F8', 'G8', 'H8']
	# create dict of board_position : word_letter
	word_pos_dict = {key: word[idx] for idx, key in enumerate(pos)}
	##    print('Word position Dict: ',word_pos_dict)

	# create dict of word_letter : point value
	word_dict = {letter: char_dict[letter] for letter in word}
	#    print('Word Dict: ',word_dict)

	# letter_multiplier_check
	new_word_dict, new_score = letter_multiplier_check(word_dict, word_pos_dict)
	#    print('Updated Word Dict: ',new_word_dict)
	#    print('Score with Letter Multiplier: ',new_score)

	# word_multiplier_check
	new_score = word_multiplier_check(word_pos_dict, new_score)
	# return both the new score based on the tiles and the position of the new letters
	return new_score, letter_pos_list


### Test Case
# ON = True
# while ON:
# 	word = input('Word: ')
# 	starting_tile = input('Starting tile: (ex: A10) ')
# 	word_direction = input('Word direction is horizontal or vertical: ')
# 	word = word.upper()
# 	print('Capitalized :', word)
# 	(multi_score, word_tile_locations) = multiplier_score(word, starting_tile, word_direction)
# 	print('Location: ', word_tile_locations)
# 	print('Score with Letter+Word Multiplier: ', multi_score)
# 	print('\n')
