import pygame


def move_top():
    hero.y -= 3


def move_bottom():
    hero.y += 3


def move_right():
    global state_hero
    hero.x += 3
    state_hero = "go_right"


def move_left():
    global state_hero

    hero.x -= 3
    state_hero = "go_left"


def state_hero_stand():
    global state_hero
    state_hero = "stand"


def sword():
    None


floor = pygame.Rect(100, 100, 600, 600)
hero = pygame.Rect(500, 500, 50, 60)
state_hero = "stand"

a = 1
