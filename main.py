import pygame, view, model, controller

we = pygame.time.Clock()
while True:
    print(model.state_hero)
    we.tick(120)
    controller.krestik()
    view.what()
