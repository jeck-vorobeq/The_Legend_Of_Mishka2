import pygame, model

screen = pygame.display.set_mode([800, 800])
lw=pygame.image.load("room/left wall(no door).png")

def what():
    pygame.draw.rect(screen, [25, 55, 20], model.floor)
    model.hero.draw_hero(screen)

    pygame.display.flip()
