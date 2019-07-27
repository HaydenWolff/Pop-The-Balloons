#########################################
# Programmer: Hayden Wolff
# Date: 4/5/2018
# File Name: pop_the_balloons.py
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
screw = pygame.image.load("screwd.png")
#screw = screw.convert_alpha()
balloon = pygame.image.load("balloon0.png")
font = pygame.font.SysFont("Ariel Black",50)
keyPressed = False

popped = 0
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
    message = ("Popped: "+str(popped))
    game_window.fill(BLACK)
    game_window.blit(background,(0,0))
    text = font.render(message, 1, BLACK)
    text2 = font.render(time, 1, BLACK)
    game_window.blit(text,(850,10))
    game_window.blit(text2,(150,10))
    pygame.mouse.set_visible(False)
    for i in range(20):
        (screwX,screwY) = pygame.mouse.get_pos()
        if balloonVisible[i] == True:
            game_window.blit(balloon, (balloonX[i],balloonY[i]))
            game_window.blit(screw, (screwX-87,screwY-25))
        elif balloonVisible[i] == False:
            balloonX[i], balloonY[i] = -50,-50
        if balloonY[i] < -10:
            balloonVisible[i] = False
        if True not in balloonVisible or popped == 20:
            gameOver()
    pygame.display.update()             # display must be updated, in order
                                        # to show the drawings
def introScreen():
    game_window.fill(BLACK)
    game_window.blit(background,(0,0))
    start_game = font.render("PRESS ANY KEY TO START", 1, BLACK)
    game_window.blit(start_game,(WIDTH//2-200,HEIGHT//2))
    pygame.display.update()
def gameOver():
    game_window.fill(BLACK)
    game_window.blit(background,(0,0))
    game_over = font.render("GAME OVER", 1, BLACK)
    endGame = font.render("Total Popped: "+str(popped)+"/"+"20",1,BLACK)
    game_window.blit(endGame, (WIDTH//2-215,400))
    game_window.blit(game_over,(WIDTH//2-150,300))
    pygame.mouse.set_visible(True)
    pygame.display.update()
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
while not keyPressed:
    introScreen()
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN:
            keyPressed = True
exit_flag = False                       #

balloonR = [0]*20                       # create lists of 20 items each
balloonX = [0]*20                       # for balloons' properties
balloonY = [0]*20                       #
balloonSPEED = [0]*20                   #
balloonCLR = [0]*20
balloonVisible = [True]*20
for i in range(20):
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = 45
    balloonSPEED[i] = randint(1,6)
    balloonCLR[i] = randint(0,255),randint(0,255),randint(0,255)
    balloon = pygame.transform.smoothscale(balloon,(balloonR[i],46))

while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i]:
                    balloonVisible[i] = False
                    popped+=1
                    #print(popped)
# move the balloons
    for i in range(20):
        balloonY[i] = balloonY[i] - balloonSPEED[i]        
# update the screen
    if keyPressed:
        time = ("Time: "+str(pygame.time.get_ticks()/1000))
        redraw_game_window()
    
    pygame.time.delay(13)
    
pygame.quit()                           # always quit pygame when done!
