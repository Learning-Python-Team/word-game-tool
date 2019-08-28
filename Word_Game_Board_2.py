'''Game Board'''

import pygame
import sys

#Colors
beige = (177,177,150)
red = (227,39,13)
pink = (249,154,140)
blue = (26,124,226)
light_blue = (148,228,245)
white = (255,255,255)
black = (0, 0, 0)

#initialize
pygame.init()
pygame.display.set_caption('Word Game Tool')
pygame.mixer.init()
display_width = 700
display_height = 680
screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
FPS = 30
screen.fill(beige)
pygame.display.update()


def rows_columns():
    right_border = 640
    bottom_border = 660

    
    #Multiplier Score Variables
    rect_width = 38
    rect_height = 38
    #Triple Word Score - Red
    rect_y_r = 61
    rect_x_r = 41
    #Triple Letter Score - Blue
    rect_y_b = 101
    rect_x_b = 241
    #Double Word Score - Pink
    rect_x_p = 81
    rect_y_p = 101
    #Double Letter Score - Light Blue
    rect_x_lb = 41
    rect_y_lb = 21

    y_lines = [[60,60], [100,100], [140,140], [180,180], [220,220], [260,260], [300,300], [340,340], [380,380], [420,420], [460,460], [500,500], [540,540], [580,580], [620,620],[660,660]] #Buffer

    x_lines = [[40,40],[80,80],[120,120],[160,160],[200,200],[240,240],[280,280],[320,320],[360,360],[400,400],[440,440],[480,480],[520,520],[560,560],[600,600],[640,640]]

    for y_1, y_2 in y_lines:
        pygame.draw.line(screen, white, (40, y_1), (right_border, y_2))

    for x_1, x_2 in x_lines:
        pygame.draw.line(screen, white, (x_1, 60), (x_2, bottom_border))
    

    # ***RED***
    triple_word_tiles = [[41, 61], [321, 61], [601, 61], [41, 341], [41, 621], [601, 341], [601, 621], [321, 621]]
    for tile_x, tile_y in triple_word_tiles:
        pygame.draw.rect(screen, red, [tile_x, tile_y, rect_width, rect_height])  # top left square, red, triple letter

    # ***BLUE***
    triple_letter_tiles = [[241, 101], [241, 261], [241, 421], [241, 581], [401, 101], [401, 261], [401, 261],
                           [401, 261], [401, 421], [401, 581], [81, 261], [561, 261], [81, 421], [561, 421]]
    for tile_x, tile_y in triple_letter_tiles:
        pygame.draw.rect(screen, blue, [tile_x, tile_y, rect_width, rect_height])

    # ***PINK***
    double_word_tiles = [[81, 101], [121, 141], [161, 181], [201, 221], [562, 101], [522, 141], [482, 181],
                         [442, 221], [81, 581], [121, 541], [161, 501], [201, 461], [562, 581], [522, 541],
                         [482, 501], [442, 461], [321, 341]]
    for tile_x, tile_y in double_word_tiles:
        pygame.draw.rect(screen, pink, [tile_x, tile_y, rect_width, rect_height])

    # ***LIGHT_BLUE***
    double_letter_tiles = [[161, 61], [481, 61], [161, 621], [481, 621], [41, 181], [41, 501], [602, 181],
                           [602, 501], [281, 141], [361, 141], [321, 181], [281, 541], [361, 541], [321, 501],
                           [121, 301], [121, 381], [161, 341], [521, 301], [521, 381], [481, 341], [281, 301],
                           [361, 301], [281, 381], [361, 381]]
    for tile_x, tile_y in double_letter_tiles:
        pygame.draw.rect(screen, light_blue, [tile_x, tile_y, rect_width, rect_height])

    pygame.display.update()

rows_columns()

def text():
    pos = (50,50),(100,100)
    message = "This is some text"
    small_font = pygame.font.SysFont('Arial', 10)
    center_font = pygame.font.SysFont('Arial', 65)
    large_font = pygame.font.SysFont('Arial', 100)
    text = center_font.render(message, True, black, (300,300,300))
    dest = (30,0)
    screen.blit(text, dest)
    

text()
pygame.display.update()
