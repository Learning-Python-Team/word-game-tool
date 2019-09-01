# handles the operation of the tool and is called by main to run it
from Word_Game_Board import pygame_setup


def board():
    pygame_setup()


def current_game_state():
    # Allows user to enter the current state of play in their game
    pass


def scoring_word():
    # Asks for word to be scored and location, validates it,
    # checks for perpendicular words on the board and multipliers, calls multiplier_score to calculate
    pass


def perpendicular_word_finder():
    # Finds any additional words that are formed from placing the user word
    pass
