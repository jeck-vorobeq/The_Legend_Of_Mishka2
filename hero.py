import pygame

class Ball():
    def __init__(self):
        self.razmer = 12

    def plus_razmer(self):
        self.razmer += 1

    def draw(self,screen):
        pygame.draw.circle(screen,[255,255,255],[120,100],self.razmer)