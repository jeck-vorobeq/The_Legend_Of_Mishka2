import time

import pygame, model,hero
from pygame import joystick

joystick.init()


# lol = joystick.Joystick(0)

# lol.init()


def krestik():
    krestik = pygame.event.get()
    model.state_hero_stand()
    for c in krestik:
        # print(c)
        if c.type == pygame.QUIT:
            exit()
        if c.type == pygame.KEYDOWN:
            if c.key == pygame.K_SPACE:
                model.a.plus_razmer()
        if c.type == pygame.MOUSEBUTTONDOWN:
            model.a =hero.Ball(10,c.pos,30)
    # value = lol.get_hat(0)
    # lalue = lol.get_button(1)
    # walue = lol.get_button(0)
    # if value == (0, 1):
    #     model.move_top()
    #
    # if value == (0, -1):
    #     model.move_bottom()
    # if value == (-1, 0):
    #
    #     model.move_left()
    #
    # if value == (1, 0):
    #     model.move_right()
    # if lalue == 1:
    #     model.shield()
    # if walue == 1:
    #     model.sword()


c = 3
