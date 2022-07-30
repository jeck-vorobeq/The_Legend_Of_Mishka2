import pygame

top1 = pygame.image.load("hero/top1.png")
top2 = pygame.image.load("hero/top2.png")
top3 = pygame.image.load("hero/top3.png")
top1 = pygame.transform.scale(top1, [154 / 2, 269 / 2])
top2 = pygame.transform.scale(top2, [154 / 2, 269 / 2])
top3 = pygame.transform.scale(top3, [154 / 2, 269 / 2])

bottom1 = pygame.image.load("hero/bottom1.png")
bottom2 = pygame.image.load("hero/bottom2.png")
bottom3 = pygame.image.load("hero/bottom3.png")
bottom1 = pygame.transform.scale(bottom1, [154 / 2, 269 / 2])
bottom2 = pygame.transform.scale(bottom2, [154 / 2, 269 / 2])
bottom3 = pygame.transform.scale(bottom3, [154 / 2, 269 / 2])
left1 = pygame.image.load("hero/left1.png")
left2 = pygame.image.load("hero/left2.png")
left3 = pygame.image.load("hero/left3.png")

left1 = pygame.transform.scale(left1, [154 / 2, 269 / 2])
left2 = pygame.transform.scale(left2, [154 / 2, 269 / 2])
left3 = pygame.transform.scale(left3, [154 / 2, 269 / 2])

right1 = pygame.transform.flip(left1, True, False)
right2 = pygame.transform.flip(left2, True, False)
right3 = pygame.transform.flip(left3, True, False)


class Hero():
    def __init__(self):
        self.rect_hero = pygame.Rect(500, 500, 50, 60)
        self.state = "go_bottom"
        self.costum = "bottom1"

    def draw_hero(self, screen):
        if self.costum == "left1":
            screen.blit(left1, self.rect_hero)
        elif self.costum == "left2":
            screen.blit(left2, self.rect_hero)
        elif self.costum == "left3":
            screen.blit(left3, self.rect_hero)

        if self.costum == "bottom1":
            screen.blit(bottom1, self.rect_hero)
        elif self.costum == "bottom2":
            screen.blit(bottom2, self.rect_hero)
        elif self.costum == "bottom3":
            screen.blit(bottom3, self.rect_hero)

        if self.costum == "right1":
            screen.blit(right1, self.rect_hero)
        elif self.costum == "right2":
            screen.blit(right2, self.rect_hero)
        elif self.costum == "right3":
            screen.blit(right3, self.rect_hero)

        if self.costum == "top1":
            screen.blit(top1, self.rect_hero)
        elif self.costum == "top2":
            screen.blit(top2, self.rect_hero)
        elif self.costum == "top3":
            screen.blit(top3, self.rect_hero)

    def change_costum_hero(self):
        if self.state == "go_left":

            if self.costum != "left1" and self.costum != "left2":
                self.costum = "left1"
            elif self.costum == "left1":
                self.costum = "left2"
            elif self.costum == "left2":
                self.costum = "left3"
        if self.state == "stand_left":
            self.costum = "left3"
        if self.state == "go_right":

            if self.costum != "right1" and self.costum != "right2":
                self.costum = "right1"
            elif self.costum == "right1":
                self.costum = "right2"
            elif self.costum == "right2":
                self.costum = "right3"

        if self.state == "stand_right":
            self.costum = "right3"

        if self.state == "go_bottom":
            if self.costum != "bottom1" and self.costum != "bottom2":
                self.costum = "bottom1"
            elif self.costum == "bottom1":
                self.costum = "bottom2"
            elif self.costum == "bottom2":
                self.costum = "bottom3"
        if self.state == "stand_bottom":
            self.costum = "bottom3"

        if self.state == "go_top":
            if self.costum != "top1" and self.costum != "top2":
                self.costum = "top1"
            elif self.costum == "top1":
                self.costum = "top2"
            elif self.costum == "top2":
                self.costum = "top3"
        if self.state == "stand_top":
            self.costum = "top3"

    def move_top(self):
        self.rect_hero.y -= 3
        self.state = "go_top"

    def move_bottom(self):
        self.rect_hero.y += 3
        self.state = "go_bottom"

    def move_right(self):
        self.rect_hero.x += 3
        self.state = "go_right"

    def move_left(self):

        self.rect_hero.x -= 3
        self.state = "go_left"
