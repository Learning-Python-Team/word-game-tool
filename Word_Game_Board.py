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

display_width = 700
display_height = 680

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
FPS = 30
screen.fill(beige)
pygame.display.update()



def rows_columns():
    y = 20 #Buffer
    x = 40

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

    drawing = True
    #draw square matrix, 40 pixels apart.
    while drawing:    
        y += 40
        pygame.draw.line(screen, white, (40, y), (right_border, y))
        pygame.draw.line(screen, white, (x, 60), (x, bottom_border))
        x += 40

        pygame.draw.line(screen, beige, (680, 60), (680, 680))
        
        #screen, color, [x,y,w,h]       ***RED***
        pygame.draw.rect(screen, red, [rect_x_r, rect_y_r, rect_width, rect_height]) #top left square, red, triple letter

        pygame.draw.rect(screen, red, [321, rect_y_r, rect_width, rect_height]) #top middle
        pygame.draw.rect(screen, red, [601, rect_y_r, rect_width, rect_height]) #top right


        pygame.draw.rect(screen, red, [rect_x_r, 341, rect_width, rect_height]) #left middle
        pygame.draw.rect(screen, red, [rect_x_r, 621, rect_width, rect_height]) #bottom left
        
        pygame.draw.rect(screen, red, [601, 341, rect_width, rect_height]) #middle right
        pygame.draw.rect(screen, red, [601, 621, rect_width, rect_height]) #bottom right
        pygame.draw.rect(screen, red, [321, 621, rect_width, rect_height]) #bottom middle

        # ***BLUE***
        pygame.draw.rect(screen, blue, [rect_x_b, rect_y_b, rect_width, rect_height]) #Blue Squares
        pygame.draw.rect(screen, blue, [rect_x_b, rect_y_b + 160, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b, rect_y_b + 320, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b, rect_y_b + 480, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 160, rect_y_b, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 160, rect_y_b + 160, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 160, rect_y_b + 160, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 160, rect_y_b + 160, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 160, rect_y_b + 320, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 160, rect_y_b + 480, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b - 160, rect_y_b + 160, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 320, rect_y_b + 160, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b - 160, rect_y_b + 320, rect_width, rect_height])
        pygame.draw.rect(screen, blue, [rect_x_b + 320, rect_y_b + 320, rect_width, rect_height])

        # ***PINK***
        pygame.draw.rect(screen, pink, [rect_x_p, rect_y_p, rect_width, rect_height]) #Pink Squares, top left
        pygame.draw.rect(screen, pink, [rect_x_p + 40, rect_y_p + 40, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 80, rect_y_p + 80, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 120, rect_y_p + 120, rect_width, rect_height])

        pygame.draw.rect(screen, pink, [rect_x_p + 481 , rect_y_p, rect_width, rect_height]) #Pink Squares, top right
        pygame.draw.rect(screen, pink, [rect_x_p + 441, rect_y_p + 40, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 401, rect_y_p + 80, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 361, rect_y_p + 120, rect_width, rect_height])

        pygame.draw.rect(screen, pink, [rect_x_p, rect_y_p + 480, rect_width, rect_height]) #Pink Squares, bottom left
        pygame.draw.rect(screen, pink, [rect_x_p + 40, rect_y_p + 440, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 80, rect_y_p + 400, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 120, rect_y_p + 360, rect_width, rect_height])

        pygame.draw.rect(screen, pink, [rect_x_p + 481, rect_y_p + 480, rect_width, rect_height]) #Pink Squares, bottom right
        pygame.draw.rect(screen, pink, [rect_x_p + 441, rect_y_p + 440, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 401, rect_y_p + 400, rect_width, rect_height])
        pygame.draw.rect(screen, pink, [rect_x_p + 361, rect_y_p + 360, rect_width, rect_height])

        pygame.draw.rect(screen, pink, [321, 341, rect_width, rect_height]) #middle
    
        # ***LIGHT_BLUE***
        #Top Row
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 120, rect_y_lb + 40, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 440, rect_y_lb + 40, rect_width, rect_height])

        #Bottom Row
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 120, rect_y_lb + 601, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 440, rect_y_lb + 601, rect_width, rect_height])

        #Outer Left
        pygame.draw.rect(screen, light_blue, [rect_x_lb, rect_y_lb + 160, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb, rect_y_lb + 480, rect_width, rect_height])

        #Outer Right
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 561, rect_y_lb + 160, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 561, rect_y_lb + 480, rect_width, rect_height])

        #Inner - Top
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 240, rect_y_lb + 120, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 320, rect_y_lb + 120, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 280, rect_y_lb + 160, rect_width, rect_height])

        #Inner - Bottom
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 240, rect_y_lb + 520, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 320, rect_y_lb + 520, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 280, rect_y_lb + 480, rect_width, rect_height])

        #Inner -  Left
        pygame.draw.rect(screen, light_blue, [rect_x_lb +80, rect_y_lb + 280, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 80, rect_y_lb + 360, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 120, rect_y_lb + 320, rect_width, rect_height])

        #Inner - Right
        pygame.draw.rect(screen, light_blue, [rect_x_lb +480, rect_y_lb + 280, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 480, rect_y_lb + 360, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb + 440, rect_y_lb + 320, rect_width, rect_height])

        #Inner - Square
        pygame.draw.rect(screen, light_blue, [rect_x_lb +240, rect_y_lb + 280, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb +320, rect_y_lb + 280, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb +240, rect_y_lb + 360, rect_width, rect_height])
        pygame.draw.rect(screen, light_blue, [rect_x_lb +320, rect_y_lb + 360, rect_width, rect_height])


        pygame.display.update()




rows_columns()
