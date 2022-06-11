import pygame,model
b=2
e=pygame.display.set_mode([800, 800])
def what():
    pygame.draw.rect(e, [240, 200, 219], model.floor)
    pygame.draw.rect(e, [200, 210, 20], model.hero)
    pygame.display.flip()





















