

import pygame as p
import math
import random

WIDTH = 300
HEIGHT = 300
X = 50
Y = 50

BACKGROUND = p.Color("light steel blue")
RADII = [150, 125, 100, 75, 20]
#150 outermost ring, 125 4th ring, 100 3rd ring, 80 2nd ring, 40 bullseye ring, 20 bullseye
RING_COLORS  = ['purple','yellow', 'green', 'blue', 'red']
NUM_DARTS = 0
PERCENTAGES = [0, 0, 0, 0, 0, 0] #1 more 0 than number of rings
SPOTS = [0, 0, 0, 0, 0, 0]
LASTBULLSEYE = 0


def draw(screen):
    p.draw.rect(screen, BACKGROUND, p.Rect(X, Y, WIDTH, HEIGHT))
    for i in range(len(RADII)):
        p.draw.circle(screen, p.Color(RING_COLORS[i]),
                      (WIDTH//2 + X, HEIGHT//2 + Y), RADII[i])
        
def throwDartRandomly(screen):
    x = random.randint(0, WIDTH) + X
    y = random.randint(0, HEIGHT) + Y
    p.draw.circle(screen, p.Color("black"), (x, y), 2)
    global NUM_DARTS
    NUM_DARTS+=1
    updatePercents(x-150, y-150)
    
def updatePercents(x, y):
    global PERCENTAGES, NUM_DARTS, SPOTS, LASTBULLSEYE
    rad = (x**2 + y**2)**.5 #distinguish between different RADII
    if rad > RADII[0]:
        SPOTS[0] = SPOTS[0] + 1
        PERCENTAGES[0] = round(SPOTS[0]/NUM_DARTS, 2)*100 #give rounded percents
        LASTBULLSEYE = LASTBULLSEYE +  1          
    elif rad < RADII[0] and rad > RADII[1]:
        SPOTS[1] = SPOTS[1] + 1
        PERCENTAGES[1] = round(SPOTS[1]/NUM_DARTS, 2)*100
        LASTBULLSEYE  = LASTBULLSEYE + 1      
    elif rad < RADII[1] and rad > RADII[2]:
        SPOTS[2] = SPOTS[2]+ 1
        PERCENTAGES[2] = round(SPOTS[2]/NUM_DARTS, 2)*100
        LASTBULLSEYE  = LASTBULLSEYE  + 1      
    elif rad < RADII[2] and rad > RADII[3]:
        SPOTS[3]= SPOTS[3]+ 1
        PERCENTAGES[3] = round(SPOTS[3]/NUM_DARTS, 2)*100
        LASTBULLSEYE = LASTBULLSEYE  + 1  
    elif rad < RADII[3] and rad > RADII[4]:
        SPOTS[4]= SPOTS[4]+ 1
        PERCENTAGES[4] = round(SPOTS[4]/NUM_DARTS, 2)*100
        LASTBULLSEYE = LASTBULLSEYE + 1   
    elif rad < RADII[4]:
        SPOTS[5] = SPOTS[5]+ 1
        PERCENTAGES[5] = round(SPOTS[5]//NUM_DARTS, 2)*100
        LASTBULLSEYE = 0 #in order for a reset this would have to be 0
    
