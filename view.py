import pygame,model,helper
b=2
screen=pygame.display.set_mode([800, 800])
left1=pygame.image.load("hero/left1.png")
left2=pygame.image.load("hero/left2.png")
left3=pygame.image.load("hero/left3.png")
left1=pygame.transform.scale(left1,[154/2,269/2])
left2=pygame.transform.scale(left2,[154/2,269/2])
left3=pygame.transform.scale(left3,[154/2,269/2])
costum="left1"

def what():
    global costum
    pygame.draw.rect(screen, [240, 200, 219], model.floor)

    if costum=="left1":
        screen.blit(left2, model.hero)
        costum="left2"
    elif costum=="left2":
        screen.blit(left3, model.hero)
        costum="left3"
    elif costum=="left3":
        screen.blit(left1, model.hero)
        costum="left1"
    pygame.display.flip()





















