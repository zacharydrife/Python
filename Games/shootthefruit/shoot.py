import pygame as pg
import pgzero as pg0
import pgzrun as pgzrun
from random import randint as randint

apple = Actor("apple")
pineapple = Actor("pineapple")
orange = Actor("orange")

time_left = 10

def draw():
    screen.clear()
    screen.draw.text("Time left: " + str(time_left), (10, 10))
    apple.draw()
    pineapple.draw()
    orange.draw()

def countdown():
    global time_left
    time_left -= 1
    if time_left == 0:
        print("Game over!")
        quit()

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

clock.schedule_interval(countdown, 1)


pgzrun.go()