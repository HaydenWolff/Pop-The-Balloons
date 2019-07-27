#########################################
# Programmer: Hayden Wolff
# Date: 4/5/2018
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################

import pygame
pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module

HEIGHT = 800
WIDTH  = 1200
game_window=pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("sky2.jpg")
background = pygame.transform.scale(background,(WIDTH,HEIGHT))
screw = pygame.image.load("screw.png")
screw = screw.convert_alpha()
##balloon = []
balloon0 = pygame.image.load("balloon0.png")
##balloon1 = pygame.image.load("balloon1.png")
##balloon2 = pygame.image.load("balloon2.png")
##balloon3 = pygame.image.load("balloon3.png")
##balloon4 = pygame.image.load("balloon4.png")
##balloon5 = pygame.image.load("balloon5.png")
##balloon6 = pygame.image.load("balloon6.png")


screwX = 0
screwY = 0

WHITE = (255,255,255)                   #
BLACK = (  0,  0,  0)                   # used colours
outline=0                               # thickness of the shapes' outline

#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    game_window.fill(BLACK)
    game_window.blit(background,(0,0))
    pygame.mouse.set_visible(False)
    for i in range(20):
        game_window.blit(balloon0, (balloonX[i],balloonY[i]))
        #pygame.draw.circle(game_window, balloonCLR[i], (balloonX[i], balloonY[i]), balloonR[i], outline)
    game_window.blit(screw, (screwX-87,screwY-25))
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings
       
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False                       #
##for i in range(6):
##    imageName = "balloon"+str(i)+".png"
##    balloon.append(imageName)
##    balloon[i] = pygame.image.load(imageName)


balloonR = [0]*20                       # create lists of 20 items each
balloonX = [0]*20                       # for balloons' properties
balloonY = [0]*20                       #
balloonSPEED = [0]*20                   #
balloonCLR = [0]*20
ballonVisible = [True]*20
for i in range(20):
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = 39
    balloonSPEED[i] = randint(1,5)
    balloonCLR[i] = randint(0,255),randint(0,255),randint(0,255)
    balloon = pygame.transform.smoothscale(balloon0,(balloonR[i],46))

while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                (cursorX,cursorY)=pygame.mouse.get_pos()
            if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i]:
                balloonX[i], balloonY[i] = 0,0
##                    for i in range(7):
##                        balloon = pygame.transform.smoothscale((str(balloon+i)),(balloonR[i],46))
                    
# move the balloons
    for i in range(20):
        balloonY[i] = balloonY[i] - balloonSPEED[i]        
    (screwX,screwY) = pygame.mouse.get_pos()
# update the screen    
    redraw_game_window()
    pygame.time.delay(20)
    
pygame.quit()                           # always quit pygame when done!
