import pygame, model, helper, time

b = 2
q = time.time()
screen = pygame.display.set_mode([800, 800])
top1 = pygame.image.load("hero/top1.png")
top2 = pygame.image.load("hero/top2.png")
top3 = pygame.image.load("hero/top3.png")
top1 = pygame.transform.scale(top1, [154 / 2, 269 / 2])
top2 = pygame.transform.scale(top2, [154 / 2, 269 / 2])
top3 = pygame.transform.scale(top3, [154 / 2, 269 / 2])

bottom1 = pygame.image.load("hero/bottom1.png")
bottom2 = pygame.image.load("hero/bottom2.png")
bottom3 = pygame.image.load("hero/bottom3.png")
bottom1 = pygame.transform.scale(bottom1, [154 / 2, 269 / 2])
bottom2 = pygame.transform.scale(bottom2, [154 / 2, 269 / 2])
bottom3 = pygame.transform.scale(bottom3, [154 / 2, 269 / 2])
left1 = pygame.image.load("hero/left1.png")
left2 = pygame.image.load("hero/left2.png")
left3 = pygame.image.load("hero/left3.png")

left1 = pygame.transform.scale(left1, [154 / 2, 269 / 2])
left2 = pygame.transform.scale(left2, [154 / 2, 269 / 2])
left3 = pygame.transform.scale(left3, [154 / 2, 269 / 2])

right1 = pygame.transform.flip(left1, True, False)
right2 = pygame.transform.flip(left2, True, False)
right3 = pygame.transform.flip(left3, True, False)

costum = "left1"


def draw_hero():
    if costum == "left1":
        screen.blit(left1, model.hero)
    elif costum == "left2":
        screen.blit(left2, model.hero)
    elif costum == "left3":
        screen.blit(left3, model.hero)

    if costum == "bottom1":
        screen.blit(bottom1, model.hero)
    elif costum == "bottom2":
        screen.blit(bottom2, model.hero)
    elif costum == "bottom3":
        screen.blit(bottom3, model.hero)

    if costum == "right1":
        screen.blit(right1, model.hero)
    elif costum == "right2":
        screen.blit(right2, model.hero)
    elif costum == "right3":
        screen.blit(right3, model.hero)

    if costum == "top1":
        screen.blit(top1, model.hero)
    elif costum == "top2":
        screen.blit(top2, model.hero)
    elif costum == "top3":
        screen.blit(top3, model.hero)

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
    pygame.draw.rect(screen, [240, 200, 219], model.floor)
    draw_hero()
    play_animation_hero()
    model.a.draw(screen)
    pygame.display.flip()
