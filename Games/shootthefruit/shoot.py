import pygame as pg
import pgzero as pg0
import pgzrun as pgzrun
from random import randint as randint

apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")

def draw():
    screen.clear()
    apple.draw()
    pineapple.draw()
    orange.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def place_pineapple():
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
    elif pineapple.collidepoint(pos):
        print("Good shot!")
        place_pineapple()
    elif orange.collidepoint(pos):
        print("Good shot!")
        place_orange()
    else:
        print("You missed!")
        quit()


place_apple()
place_pineapple()
place_orange()

pgzrun.go()