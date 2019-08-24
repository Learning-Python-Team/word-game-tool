'''Game Board'''
"This is just a start. It needs a lot of work."

import re
import pygame

#Colors
beige = (177,177,150)
red = (227,39,13)
pink = (249,154,140)
blue = (26,124,226)
light_blue = (148,228,245)
white = (255,255,255)

#initialize
class Main_loop():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Word Game Tool')
        pygame.mixer.init()
        display_width = 600
        display_height = 600
        self.screen = pygame.display.set_mode((display_width, display_height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.screen.blit(self.background,(0,0))
        clock = pygame.time.Clock()
        FPS = 30
        self.screen.fill(beige)
        pygame.display.update()

Main_loop()

class Board(object):
    def __init_(self):
        #Use text to write Double, triple, word and letter scores on board
        self.font_small = pygame.font.SysFont('Arial', 50)
        #self.draw = pygame.draw.line(screen, color, x, y)

        #empty list to append to later
        self.board = []
        self.x
        self.y
        self.surface = pygame.Surface()
            
        pygame.draw.line(self.surface, white, (self.x, self.y))

def game_loop():
    pause = False
    while not pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        Board()
        break
game_loop()






