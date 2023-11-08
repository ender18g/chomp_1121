import random
import pygame
from math import pi, cos, sin, atan2, atan

import pygame.mouse


class Fish(pygame.sprite.Sprite):
    def __init__(self,screen,score):
        super().__init__()
        self.image = pygame.image.load('assets/images/fishTile_079.png')
        self.image = pygame.transform.flip(self.image, 1,0)
        # self.x_speed = random.random() * 5
        # self.y_speed = random.random() * 3
        self.speed = random.random() * 5
        # fish just has an angle of travel, theta
        self.theta = pi
        self.rect = self.image.get_rect()
        # change these values
        self.x = screen.get_width()
        self.y = random.randint(100, screen.get_height())
        self.rect.y = self.y
        self.screen = screen
        self.dead_timer = 0
        self.score = score  # SCORE IS A LIST WITH ONE ITEM!
        self.has_scored = 0


    def update(self):
        m1, m2, m3 = pygame.mouse.get_pressed()

        # only update theta IF button pressed
        if m1:
            # get the position of them mouse!
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # get the delta x, delt y
            delta_x = mouse_x - self.x
            delta_y = mouse_y - self.y

            # change the angle (theta) of the fish!
            self.theta = atan2(delta_y,delta_x)


        # move the fish with it's speed
        self.x = self.x + self.speed * cos(self.theta)
        self.y = self.y + self.speed * sin(self.theta)

        # update the rectangle
        self.rect.x = self.x
        self.rect.y = self.y

        # if the fish goes off top, come back to the bottom



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










