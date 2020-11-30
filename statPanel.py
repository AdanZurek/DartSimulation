
#statisticspanel

import pygame as p
import dartboard
import buttonPanel
from dartboard import LASTBULLSEYE

WIDTH = 760
HEIGHT = 600
X = 400
Y = 50
BACKGROUND = p.Color("gray")

def draw(screen):
    panel = p.Rect(X, Y, WIDTH, HEIGHT) #red white blue green yellow purple
    p.draw.rect(screen, BACKGROUND, panel)
    #adding text to pygame screen
    font = p.font.SysFont("Arial", 30)
    text = ["Total darts thrown: " + str(dartboard.NUM_DARTS),
            "",
            "Darts since last bullseye: " + str(dartboard.LASTBULLSEYE),
            "",
            "Total darts missed: " + str(dartboard.SPOTS[0]),
            "",
            "Bullseye(red) Count: " + str(dartboard.SPOTS[5]),
            "",
            "Blue Count: " + str(dartboard.SPOTS[4]),
            "",
            "Green Count: " + str(dartboard.SPOTS[3]),
            "",
            "Yellow Count: " + str(dartboard.SPOTS[2]),
            "",
            "Purple Count: " + str(dartboard.SPOTS[1]),
            "",
            "",
            "PERCENTAGES",
            "",
            "Missed darts: " + str(dartboard.PERCENTAGES[0]) +  "%",
            "",
            "Bullseye(red): " + str(dartboard.PERCENTAGES[5]) +   "%",
            "",
            "Blue: " + str(dartboard.PERCENTAGES[4])  + "%",
            "",        
            "Green: " + str(dartboard.PERCENTAGES[3]) + "%",
            "",
            "Yellow: " + str(dartboard.PERCENTAGES[2]) + "%",
            "",
            "Purple: " + str(dartboard.PERCENTAGES[1]) + "%"]
            
    
    for i in range(len(text)):
        textObject = font.render(text[i], 0, p.Color("black"))
        textLocation = panel.move(5, 20*i)
        screen.blit(textObject, textLocation)
    # keep track of how many darts have been thrown since last bullseye


    
    

