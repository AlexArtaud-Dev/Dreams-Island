from pygame import image
from pygame.sprite import Sprite


class Vegetation(Sprite):
    def __init__(self, x: int, y: int, path: str):
        super().__init__()
        self.image = image.load(path)
        self.rect = self.image.get_rect()
        self.rect.center = self.rect.center
        self.rect.centerx = x
        self.rect.centery = y
