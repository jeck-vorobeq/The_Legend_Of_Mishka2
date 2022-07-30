import pygame, model, time

b = 2
q = time.time()
screen = pygame.display.set_mode([1900, 950])


costum = "left1"






def play_animation_hero():
    global q
    qtime = (time.time() - q)
    if qtime >= 0.2:
        q = time.time()
        model.hero.change_costum_hero()


def what():
    model.hero.draw_hero(screen)

    #draw_hero()
    play_animation_hero()
    pygame.display.flip()
