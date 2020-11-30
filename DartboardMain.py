
import pygame as p
import dartboard
import buttonPanel
import statPanel
from dartboard import PERCENTAGES, LASTBULLSEYE

WIDTH = 800
HEIGHT = 700
BACKGROUND = p.Color("red")
MAX_FPS = 30

def main():
    global throwing
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BACKGROUND)
    p.display.set_caption("Dart Sim V. 1")
    clock = p.time.Clock()
    dartboard.draw(screen)
    buttons = buttonPanel.draw(screen)
    running = True
    throwing = False
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            if e.type == p.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(e.pos): # start button
                    throwing = True
                    p.draw.rect(screen, p.Color("light green"), buttons[0])
                    p.draw.rect(screen, p.Color("red"), buttons[1])
                    p.draw.rect(screen, p.Color("blue"), buttons[2])
                elif buttons[1].collidepoint(e.pos): # stop button
                    throwing = False
                    p.draw.rect(screen, p.Color("green"), buttons[0])
                    p.draw.rect(screen, p.Color("tomato"), buttons[1])
                    p.draw.rect(screen, p.Color("blue"), buttons[2])
                elif buttons[2].collidepoint(e.pos): # reset button
                    reset(screen)
                    p.draw.rect(screen, p.Color("green"), buttons[0])
                    p.draw.rect(screen, p.Color("red"), buttons[1])
                    p.draw.rect(screen, p.Color("cyan"), buttons[2])  
                    
                    
             
        if throwing:
                dartboard.throwDartRandomly(screen)
        statPanel.draw(screen)
        buttonPanel.draw(screen)
        p.display.flip()
        clock.tick(MAX_FPS)
                
                

def reset(screen):
    global throwing #add this to main()
    dartboard.draw(screen)
    throwing = False
    dartboard.NUM_DARTS = 0 
    dartboard.LASTBULLSEYE = 0
    dartboard.PERCENTAGES = [0, 0, 0, 0, 0, 0]
    dartboard.SPOTS = [0, 0, 0, 0, 0, 0] #reset count in all rings
    

main()
