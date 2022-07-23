import hero,pygame

a=hero.Ball(10,[420,500],30)

def move_top():
    global state_hero
    hero.y -= 3
    state_hero = "go_top"

def move_bottom():
    global state_hero
    hero.y += 3
    state_hero = "go_bottom"


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
    if state_hero == "go_left":
        state_hero = "stand_left"

    if state_hero == "go_right":
        state_hero = "stand_right"

    if state_hero == "go_bottom":
        state_hero = "stand_bottom"

    if state_hero == "go_top":
        state_hero = "stand_top"



def sword():
    None


floor = pygame.Rect(100, 100, 600, 600)
hero = pygame.Rect(500, 500, 50, 60)
state_hero = "stand_left"


