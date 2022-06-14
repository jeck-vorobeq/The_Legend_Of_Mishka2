import pygame,model,helper
b=2
screen=pygame.display.set_mode([800, 800])
bottom=pygame.image.load("hero/bottom.jpg")
#bottom=helper.izmeni_kartinku(bottom,50,60,[237,28,36],0)
def what():
    pygame.draw.rect(screen, [240, 200, 219], model.floor)
    screen.blit(bottom,model.hero)
    pygame.display.flip()





















