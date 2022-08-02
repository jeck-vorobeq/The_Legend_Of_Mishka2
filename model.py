import hero as hero_mod,pygame






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






floor = pygame.Rect(100, 100, 600, 600)
hero=hero_mod.Hero(500,5)
hero2=hero_mod.Hero(50,5,6)

