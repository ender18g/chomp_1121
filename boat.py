import pygame
import random

class Boat(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        #self.image = pygame.Surface((150,50))
        #self.image.fill((0,0,220))
        self.image = pygame.image.load('assets/images/boat.png')
        self.image = pygame.transform.scale_by(self.image, 0.2)
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width()/2
        self.rect.y = 0
        self.velocity = -1

    def update(self):
        self.rect.x += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)





