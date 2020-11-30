
#buttonPanel

import pygame as p
from turtledemo.penrose import star

WIDTH = 300
HEIGHT = 150
X = 50
Y = 400
BACKGROUND = p.Color('red')

def draw(screen):
    panel = p.Rect(X, Y, WIDTH, HEIGHT)
    p.draw.rect(screen, BACKGROUND, panel)
    button = p.Rect(0, 0, WIDTH//3, HEIGHT//2)
    
    startButton = button.clamp(panel).move(0, HEIGHT//4)
    font = p.font.SysFont("Times New Roman", 30, 1)
    text = ["START"]
    textObjectGreen = font.render(text[0], 0, p.Color("black"))
    textLocation = startButton
    p.draw.rect(screen, p.Color("green"), startButton)
    screen.blit(textObjectGreen, textLocation)
    
    stopButton = button.clamp(panel).move(WIDTH//3, HEIGHT//4)
    font = p.font.SysFont("Times New Roman", 30, 1)
    text = ["STOP"]
    textObjectRed = font.render(text[0], 0, p.Color("black"))
    textLocation = stopButton
    p.draw.rect(screen, p.Color("red"), stopButton)
    screen.blit(textObjectRed, textLocation)
    
    
    resetButton = button.clamp(panel).move(2*WIDTH // 3, HEIGHT//4)
    font = p.font.SysFont("Times New Roman", 30, 1)
    text = ["RESET"]
    textObjectBlue = font.render(text[0], 0, p.Color("black"))
    textLocation = resetButton
    p.draw.rect(screen, p.Color("blue"), resetButton)
    screen.blit(textObjectBlue, textLocation)
    return startButton, stopButton, resetButton

    p.draw.rect(screen, p.Color("light green"), startButton)
    p.draw.rect(screen, p.Color("blue"), resetButton)
    p.draw.rect(screen, p.Color("red"), stopButton)
    return startButton, stopButton, resetButton



    
    

