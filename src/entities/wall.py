import pygame
from pygame.sprite import Sprite

SIZE_X = 18
SIZE_Y = 17


class Wall(Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()

        self.image = pygame.Surface((SIZE_X, SIZE_Y))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * SIZE_X
        self.rect.y = y * SIZE_Y
