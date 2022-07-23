import pygame,random



class Ball():
    def __init__(self,razmer,where,prirost):
        self.razmer = razmer
        self.where= where
        self.prirost=prirost
        self.r = random.randint(1, 255)
        self.g = random.randint(1, 255)
        self.b = random.randint(1, 255)
    def plus_razmer(self):
        self.razmer += self.prirost

    def draw(self,screen):

        pygame.draw.circle(screen,[self.r,self.g,self.b],self.where,self.razmer)