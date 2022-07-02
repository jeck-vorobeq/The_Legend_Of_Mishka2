import pygame, model, helper, time

b = 2
q = time.time()
screen = pygame.display.set_mode([800, 800])
left1 = pygame.image.load("hero/left1.png")
left2 = pygame.image.load("hero/left2.png")
left3 = pygame.image.load("hero/left3.png")
left1 = pygame.transform.scale(left1, [154 / 2, 269 / 2])
left2 = pygame.transform.scale(left2, [154 / 2, 269 / 2])
left3 = pygame.transform.scale(left3, [154 / 2, 269 / 2])
right1=pygame.transform.flip(left1,True,False)
right2=pygame.transform.flip(left2,True,False)
right3=pygame.transform.flip(left3,True,False)

costum = "left1"


def draw_hero():

    if costum == "left1":
        screen.blit(left1, model.hero)
    elif costum == "left2":
        screen.blit(left2, model.hero)
    elif costum == "left3":
        screen.blit(left3, model.hero)
    if costum == "right1":
        screen.blit(right1, model.hero)
    elif costum == "right2":
        screen.blit(right2, model.hero)
    elif costum == "right3":
        screen.blit(right3, model.hero)

def change_costum_hero():
    global costum
    if model.state_hero=="go_left":

        if costum == "left1":

            costum = "left2"
        elif costum == "left2":

            costum = "left3"
        elif costum == "left3":

            costum = "left1"
    if model.state_hero=="go_right":

        if costum != "right1" and costum!="right2":

            costum = "right1"
        elif costum == "right1":

            costum = "right2"
        elif costum == "right2":
            costum = "right3"
    if model.state_hero=="stand":
        costum= "left3"



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
    pygame.display.flip()
