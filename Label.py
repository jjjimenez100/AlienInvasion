from pygame.sprite import Sprite
import pygame

class Label(Sprite):
    def __init__(self, text, size, width, height, y):
        Sprite.__init__(self)
        self.width = width
        self.y = y
        self.text = text
        self.size = size
    def update(self):
        self.image = pygame.font.SysFont("freesansbold.ttf", self.size).render(self.text, True, (50, 108, 131))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.width // 2
        self.rect.centery = self.y