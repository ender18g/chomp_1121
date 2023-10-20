import pygame
from random import randint

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    puffer_tile = pygame.image.load('assets/images/puffer_fish.png')
    water_tile = pygame.image.load('assets/images/fishTile_089.png')
    sand_top_tile = pygame.image.load('assets/images/fishTile_021.png')
    sand_tile = pygame.image.load('assets/images/fishTile_126.png')
    plant_tile = pygame.image.load('assets/images/fishTile_032.png')
    # get tile size info
    tile_width = water_tile.get_width()
    tile_height = water_tile.get_height()
    # make a background
    background = pygame.Surface((WIDTH,HEIGHT))
    # draw water tiles
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(water_tile, (x,y))
    # draw sand tile
    for x in range(0,WIDTH,tile_width):
        background.blit(sand_tile, (x,HEIGHT-tile_height))
    # draw sand top tile
    for x in range(0,WIDTH,tile_width):
        background.blit(sand_top_tile, (x,HEIGHT-2*tile_height))
    # draw some plants!
    num_plants = 6
    for p in range(num_plants):
        background.blit(plant_tile,
                        (randint(0, WIDTH),randint(HEIGHT-3*tile_height, HEIGHT-1*tile_height)))
    return background