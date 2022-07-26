import pygame, model, time

b = 2
q = time.time()
screen = pygame.display.set_mode([1900, 950])


costum = "left1"




def change_costum_hero():
    global costum
    if model.state_hero == "go_left":

        if costum != "left1" and costum != "left2":
            costum = "left1"
        elif costum == "left1":
            costum = "left2"
        elif costum == "left2":
            costum = "left3"
    if model.state_hero == "stand_left":
        costum = "left3"
    if model.state_hero == "go_right":

        if costum != "right1" and costum != "right2":
            costum = "right1"
        elif costum == "right1":
            costum = "right2"
        elif costum == "right2":
            costum = "right3"

    if model.state_hero == "stand_right":
        costum = "right3"

    if model.state_hero == "go_bottom":
        if costum != "bottom1" and costum != "bottom2":
            costum = "bottom1"
        elif costum == "bottom1":
            costum = "bottom2"
        elif costum == "bottom2":
            costum = "bottom3"
    if model.state_hero == "stand_bottom":
        costum = "bottom3"

    if model.state_hero == "go_top":
        if costum != "top1" and costum != "top2":
            costum = "top1"
        elif costum == "top1":
            costum = "top2"
        elif costum == "top2":
            costum = "top3"
    if model.state_hero == "stand_top":
        costum = "top3"


def play_animation_hero():
    global q
    qtime = (time.time() - q)
    if qtime >= 0.2:
        q = time.time()
        change_costum_hero()


def what():
    model.hero.draw_hero(screen)
    #draw_hero()
    #play_animation_hero()
    pygame.display.flip()
