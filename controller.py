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
    if value==(0,1):
        model.move_top()
        lol.rumble(70,71,5)
        lol.stop_rumble()
    if value == (0, -1):
        model.move_bottom()
        lol.rumble(70, 71, 5)
        lol.stop_rumble()
    if value == (1, 0):
        model.move_left()
        lol.rumble(70, 71, 5)
        lol.stop_rumble()
    if value == (-1, 0):
        model.move_right()
        lol.rumble(70, 71, 5)
        lol.stop_rumble()





c=3