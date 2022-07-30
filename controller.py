import time

import pygame, model,hero
from pygame import joystick

joystick.init()


lol = joystick.Joystick(0)
lol.init()


def krestik():
    krestik = pygame.event.get()
    #model.state_hero_stand()
    for c in krestik:
        # print(c)
        if c.type == pygame.QUIT:
            exit()

    value = lol.get_hat(0)

    if value == (0, 1):
        model.hero.move_top()

    if value == (0, -1):
        model.hero.move_bottom()
    if value == (-1, 0):

        model.hero.move_left()

    if value == (1, 0):
        model.hero.move_right()



c = 3
