# Example file showing a basic pygame "game loop"
import pygame
from helpers import *

import random
class Fish():
    def __init__(self,screen):
        self.image = pygame.image.load('assets/images/fishTile_079.png')
        self.image = pygame.transform.flip(self.image, 1,0)
        self.speed = random.randint(1,5)
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



# pygame setup
pygame.init()
# make a clock
clock = pygame.time.Clock()

# set the resolution of our game window
WIDTH = 1080
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Make my background once!
background = make_background(screen)

print(pygame.font.get_fonts())
# declare a Font
game_font = pygame.font.SysFont('impact', 120)

blue_fish_img = pygame.image.load('assets/images/fishTile_077.png')
blue_fish_img = pygame.transform.flip(blue_fish_img,1,0)
blue_fish_x = WIDTH

fish1 = Fish(screen)



running = True
while running:
    # move my fish to the left by 1 pixel
    blue_fish_x -=3
    fish1.update()

    # make sure my fish is not off the left of the screen
    if blue_fish_x <= 0-blue_fish_img.get_width():
        blue_fish_x=WIDTH


    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the background on the screen
    screen.blit(background, (0, 0))
    # draw text
    font_surface = game_font.render('CHOMP',1,(199, 23, 4))
    center_surfaces(screen, font_surface)

    # blit our blue fish
    screen.blit(blue_fish_img, (blue_fish_x, HEIGHT/2))
    fish1.draw()

    clock.tick(60) # run at 60 FPS

    pygame.display.set_caption(f"CHOMP {clock.get_fps():3}")

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()










