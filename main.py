import pygame, view, model, controller

we = pygame.time.Clock()
while True:
    print(model.state_hero)
    we.tick(60)
    controller.krestik()
    view.what()
