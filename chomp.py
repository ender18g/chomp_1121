# Example file showing a basic pygame "game loop"
import pygame
from helpers import *
from fish import Fish
from boat import Boat
from grenade import Grenade

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

# make our fish group
fish_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()

# make a boat instance
my_boat = Boat(screen)
boat_group = pygame.sprite.Group()
boat_group.add(my_boat)

# make fish and add to group
num_fish = 100
[fish_group.add(Fish(screen)) for n in range(num_fish) ]


running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                my_boat.velocity += 1
            if event.key == pygame.K_LEFT:
                my_boat.velocity -= 1
            if event.key == pygame.K_DOWN:
                # if less than 3 grenades exist drop a grenade if you get a space
                if len(grenade_group) < 3:
                    grenade_group.add(Grenade(my_boat.rect.midbottom))
            if event.key ==pygame.K_SPACE:
                # spacebar detonates all grenades
                [g.boom() for g in grenade_group]



    # update my fish
    fish_group.update()
    boat_group.update()
    grenade_group.update()

    # draw the background on the screen
    screen.blit(background, (0, 0))
    # only draw CHOMP in first 3 seconds of game
    if pygame.time.get_ticks() < 3000:
        # draw text
        font_surface = game_font.render('CHOMP',1,(199, 23, 4))
        center_surfaces(screen, font_surface)

    grenade_group.draw(screen)
    # draw our fish
    fish_group.draw(screen)
    # draw the boat
    boat_group.draw(screen)


    clock.tick(60) # run at 60 FPS

    pygame.display.set_caption(f"CHOMP {clock.get_fps():.0}")

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()










