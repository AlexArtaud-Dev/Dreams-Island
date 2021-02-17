import pygame
from pygame.sprite import Sprite

from src.entities.player.direction import Direction


class Weapon(object):
    def __init__(self, name: str, damages: int, rotate: bool, max_range: int,
                 velocity: int, rate: int, bullet_path: str):
        super().__init__()

        self.rotate = rotate
        self.damages = damages

        self.velocity = velocity
        self.max_range = max_range
        self.rate = rate

        self.name = name

        self.bullet_path = bullet_path

        self.bullets = pygame.sprite.Group()

    def remove_projectiles(self):
        self.bullets = self.bullets.empty()

    def fire(self, x: int, y: int, direction: Direction):
        self.bullets.add(Bullet(self, x, y, direction))

    def get_hits(self, sprite: Sprite) -> list[Sprite]:
        return pygame.sprite.spritecollide(sprite, self.bullets, False)


class Bullet(Sprite):
    def __init__(self, weapon: Weapon, x: int, y: int, direction: Direction):
        super().__init__()

        self.weapon = weapon

        self.direction = direction

        self.image = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load(self.weapon.bullet_path), (35, 35)), self.direction.value[2])

        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.del_inc = self.weapon.max_range

        self.angle = 0

    def remove(self):
        self.weapon.bullets.remove(self)

    def update(self, dt: int):
        self.del_inc -= self.weapon.velocity

        if self.del_inc <= 0:
            self.remove()

        self.rect.centerx += self.direction.value[0]*self.weapon.velocity
        self.rect.centery += self.direction.value[1]*self.weapon.velocity

        self.image = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load(self.weapon.bullet_path), (35, 35)), self.direction.value[2])

        if self.weapon.rotate:
            self.rotation_projectile()

    def rotation_projectile(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
