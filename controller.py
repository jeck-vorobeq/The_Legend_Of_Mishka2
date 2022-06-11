import time

import pygame,model
from pygame import joystick

joystick.init()

lol=joystick.Joystick(0)

lol.init()

def krestik():

    krestik = pygame.event.get()

    for c in krestik:
        #print(c)
        if c.type==pygame.QUIT:
            exit()
    value=lol.get_hat(0)
    lalue=lol.get_button(1)
    walue = lol.get_button(0)
    print(lalue)
    if value==(0,1):
        model.move_top()
        lol.rumble(1,1,2)
        lol.stop_rumble()
    if value == (0, -1):
        model.move_bottom()
        lol.rumble(1, 1, 2)
        lol.stop_rumble()
    if value == (1, 0):
        model.move_left()
        lol.rumble(1, 1, 2)
        lol.stop_rumble()
    if value == (-1, 0):
        model.move_right()
        lol.rumble(1, 1, 2)
        lol.stop_rumble()
    if lalue == 1:
        model.shield()
        lol.rumble(50, 51, 1)
        lol.stop_rumble()
    if walue == 1:
        model.sword()
        lol.rumble(50, 51, 1)
        lol.stop_rumble()




c=3