import pygame
from math import sqrt
class Grenade(pygame.sprite.Sprite):
    def __init__(self,pos, fish_group):
        super().__init__()
        # attributes  image, rect, velocity
        self.image = pygame.image.load('assets/images/rocket1.png')
        self.image = pygame.transform.flip(self.image, 0, 1)
        self.image = pygame.transform.scale_by(self.image, 0.7)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity = 1
        self.boom_time = 0
        self.fish_group = fish_group
        self.kill_radius = 100
        self.collision_radius = 30

    def update(self):
        # grenade moves down
        self.rect.y += self.velocity
        # check if the grenade has been boomed, then delete after 1 second
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time > 1000:
                # grenade dies
                self.kill()
        # check to see if we hit any fish IF we haven't already boomed!
        if not self.boom_time:
            self.check_fish_hit()

    def boom(self):
        self.boom_time = pygame.time.get_ticks()
        # grenade changes its image
        self.image = pygame.image.load('assets/images/explosion1.png')
        self.velocity = 0
        self.kill_fish()


    def kill_fish(self):
        # get our grenade location
        grenade_coord = self.rect.center
        # loop over each fish in fish group
        for fish in self.fish_group:
            # calc the distance to that fish from the grenade
            fish_coord = fish.rect.center
            # if it's close, kill it
            if self.get_distance(grenade_coord,fish_coord)< self.kill_radius:
                #fish.kill()
                # turn that fish into a skeleton!
                fish.skeleton()

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return sqrt( (x2-x1)**2 + (y2-y1)**2 )

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return (self.get_distance(coord1,coord2) < self.collision_radius)


    def check_fish_hit(self):
        # check for collisions with the fish group use spritecollide
        hit_fish_list = pygame.sprite.spritecollide(self, self.fish_group, 0,  collided=self.get_sprite_distance )
        # if we find a collision, call fish.skeleton()
        for f in hit_fish_list:
            f.skeleton()
        # boom the grenade if the hit fish list not empty
        if hit_fish_list:
            self.boom()








