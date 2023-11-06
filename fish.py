import random
import pygame
class Fish(pygame.sprite.Sprite):
    def __init__(self,screen,score):
        super().__init__()
        self.image = pygame.image.load('assets/images/fishTile_079.png')
        self.image = pygame.transform.flip(self.image, 1,0)
        self.speed = random.random() * 5
        self.rect = self.image.get_rect()
        # change these values
        self.x = screen.get_width()
        self.rect.y = random.randint(100, screen.get_height())
        self.screen = screen
        self.dead_timer = 0
        self.score = score  # SCORE IS A LIST WITH ONE ITEM!
        self.has_scored = 0


    def update(self):
        self.x -= self.speed
        if self.x <0:
            self.x = self.screen.get_width()
        self.rect.x = self.x

        # if the fish turned into a skeleton, eventually remove it
        if self.dead_timer and (pygame.time.get_ticks() - self.dead_timer>1000):
            self.kill()

    def skeleton(self):
        self.image = pygame.image.load('assets/images/fishTile_091.png')
        self.image = pygame.transform.flip(self.image, 1,0)
        self.dead_timer = pygame.time.get_ticks()

        # update the score only if you haven't already added to the score
        if not self.has_scored:
            self.score[0] += 1
            self.has_scored = 1
            print(self.score)










