import pygame

from src.entities.vegetations.vegetation import Vegetation


SIZE_X = 17
SIZE_Y = 16


class Three(Vegetation):
    def __init__(self, x: int, y: int, path: str):
        super().__init__(x, y, path)

        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * SIZE_X
        self.rect.y = y * SIZE_Y
