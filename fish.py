import random
import pygame
class Fish():
    def __init__(self,screen):
        self.image = pygame.image.load('assets/images/fishTile_079.png')
        self.image = pygame.transform.flip(self.image, 1,0)
        self.speed = random.random() * 5
        self.x = screen.get_width()
        self.y = random.randint(0,screen.get_height())
        self.screen = screen

    def update(self):
        # move the fish to the left
        self.x -=self.speed
        if self.x<0:
            self.x = self.screen.get_width()

    def draw(self):
        # blit the fish on the screen
        self.screen.blit(self.image, (self.x,self.y))