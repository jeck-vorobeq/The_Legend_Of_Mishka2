import pygame


def move_top():
    hero.y -= 5


def move_bottom():
    hero.y += 5


def move_right():
    hero.x += 5


def move_left():
    global state_hero
    state_hero="stand"
    hero.x -= 5
    state_hero="go_left"

def shield():
    None


def sword():
    None


floor = pygame.Rect(100, 100, 600, 600)
hero = pygame.Rect(500, 500, 50, 60)
state_hero="stand"


a = 1
