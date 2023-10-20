# Example file showing a basic pygame "game loop"
import pygame
from helpers import *

# this function will take 2 surface and center the 2nd surface on the first one
def center_surfaces(bg, fg):
    # get the bg width and height
    bg_width = bg.get_width()
    bg_height = bg.get_height()
    # get the front surface width and height
    fg_width = fg.get_width()
    fg_height = fg.get_height()
    # blit the text on the surface
    bg.blit(fg, (bg_width/2 - fg_width/2, bg_height/2-fg_height/2 ))

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


running = True
while running:
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



    clock.tick()
    pygame.display.set_caption(f"CHOMP {clock.get_fps():3}")

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()










