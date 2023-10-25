import pygame
class Grenade(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        # attributes  image, rect, velocity
        self.image = pygame.image.load('assets/images/grenade2.png')
        self.image = pygame.transform.scale_by(self.image, 0.05)
        self.rect = self.image.get_rect()
        self.rect.midtop = pos
        self.velocity = 1
        self.boom_time = 0

    def update(self):
        # grenade moves down
        self.rect.y += self.velocity
        # check if the grenade has been boomed, then delete after 1 second
        if self.boom_time:
            if pygame.time.get_ticks() - self.boom_time > 1000:
                # grenade dies
                self.kill()
    def boom(self):
        self.boom_time = pygame.time.get_ticks()
        # grenade changes its image
        self.image = pygame.image.load('assets/images/explosion1.png')
        self.velocity = 0








