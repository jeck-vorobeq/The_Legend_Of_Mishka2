import pygame, view, model, controller

we = pygame.time.Clock()
while True:

    we.tick(120)
    controller.krestik()
    view.what()
