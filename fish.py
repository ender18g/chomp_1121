import random
import pygame
class Fish(pygame.sprite.Sprite):
    def __init__(self,screen):
        super().__init__()
        self.image = pygame.image.load('assets/images/fishTile_079.png')

        self.image = pygame.transform.flip(self.image, 1,0)
        self.speed = random.random() * 5
        self.rect = self.image.get_rect()
        # change these values
        self.x = screen.get_width()
        self.rect.y = random.randint(0, screen.get_height())
        self.screen = screen

    def update(self):
        self.x -= self.speed
        if self.x <0:
            self.x = self.screen.get_width()
        self.rect.x = self.x








