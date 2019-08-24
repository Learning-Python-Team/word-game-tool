'''Game Board'''
"This is just a start. It needs a lot of work."

import pygame

#Colors
beige = (177,177,150)
red = (227,39,13)
pink = (249,154,140)
blue = (26,124,226)
light_blue = (148,228,245)
white = (255,255,255)

#initialize
pygame.init()
pygame.display.set_caption('Word Game Tool')
pygame.mixer.init()
display_width = 600
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
FPS = 30
screen.fill(beige)
pygame.display.update()

def rows_columns():
    y = 0
    x = 0
    drawing = True
    while drawing:
        for i in range(3):
            y += 40
            pygame.draw.line(screen, white, (0, y), (600, y))
            x += 40
            pygame.draw.line(screen, white, (x, 0), (x, 600))
            pygame.display.update()

rows_columns()
