# Coin Collector

import pygame as pg
import pgzero as pg0
import pgzrun as pgzrun
from random import randint as randint

width = 400
height = 400
title = "Coin Collector"

score = 0

game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

hedgehog = Actor("hedgehog")

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    if game_over:
        screen.fill("pink")
        screen.draw.text("Final score: " + str(score), color="black", topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (width - 20))
    coin.y = randint(20, (height - 20))

def time_up():
    global game_over
    game_over = True


def update():
    global score

    if keyboard.left:
        fox.x -= 4
    elif keyboard.right:
        fox.x += 4
    elif keyboard.up:
        fox.y -= 4
    elif keyboard.down:
        fox.y += 4

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score += 10
        place_coin()


clock.schedule(time_up, 10.0)
place_coin()



pgzrun.go()

