import pygame
import time
import sys

print(f" the quit event is type {pygame.QUIT}")
pygame.init()


screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Chomp!")
screen.fill((114,159,255))
pygame.draw.rect(screen, (100,25,0), (0, 380, 400, 400))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (200,200,64,64))
pygame.draw.rect(screen, (0,255,0), (200,200, 50,50))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for playing")
            pygame.quit()
            sys.exit()

        pygame.display.flip()