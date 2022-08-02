import pygame, model

screen = pygame.display.set_mode([1900, 950])


def what():
    model.hero.draw_hero(screen)
    model.hero2.draw_hero(screen)
    pygame.display.flip()
