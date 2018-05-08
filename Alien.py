from pygame.sprite import Sprite
import pygame
import random

class Alien(Sprite):
    width : int
    height : int
    # True - right, False - left
    spawnDirection : bool
    def __init__(self, width, height):
        Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load("resources/images/IDLE.PNG"), (50, 50))
        self.rect = self.image.get_rect()
        self.spawnDirection = random.randrange(1,3) % 2 == 0
        if(self.spawnDirection):
            self.rect.x = random.randrange(self.width, self.width+20)
        else:
            self.rect.x = random.uniform(0, -20)
        self.rect.y = (height // 2) + 60

    def update(self):
        if(self.spawnDirection):
            self.rect.x -= 1
        else:
            self.rect.x += 1
