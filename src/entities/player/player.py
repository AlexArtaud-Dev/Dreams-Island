from enum import Enum

import pygame
from pygame import image
from pygame.sprite import Sprite, Group
from pygame.surface import Surface

from src.entities.consumable import Consumable
from src.entities.player.direction import Direction
from src.entities.flask import Flask
from src.entities.player.weapon import Weapon
from src.settings import *


class Perso(Enum):
    DEFAULT = [
        ['./assets/perso/default/bas1.png', './assets/perso/default/bas2.png', './assets/perso/default/bas3.png'],
        ['./assets/perso/default/droite1.png', './assets/perso/default/droite2.png', './assets/perso/default/droite3.png'],
        ['./assets/perso/default/gauche1.png', './assets/perso/default/gauche2.png', './assets/perso/default/gauche3.png'],
        ['./assets/perso/default/haut1.png', './assets/perso/default/haut2.png', './assets/perso/default/haut3.png']
    ]


class Control(object):
    def __init__(self, left, right, up, down, fire):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.fire = fire


class Player(Sprite):
    def __init__(self, name: str, velocity: int, perso: Perso, x: int, y: int, control: Control):
        super().__init__()

        self.control = control

        self.name = name
        self.seeds = 0
        self.tiredness = 0

        self.health = 100
        self.health_img = pygame.image.load("./assets/perso/heart.png")
        self.health_img = pygame.transform.scale(self.health_img, (8, 8))

        self.consumables = []
        self.flasks = []

        self.weapon = Weapon("Stick", 1, False, 2, 1, 500, './assets/weapons/stick.png')

        self.perso = perso

        self.velocity = velocity

        self.image = image.load(self.perso.value[0][0])

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = Direction.TOP
        self.enemie = None

        self.walls = Group()

        self.last_shot = pygame.time.get_ticks()

    def set_enemie(self, player: "Player"):
        self.enemie = player

    def update_hearts(self, surface: Surface):
        y = self.rect.centery-self.rect.size[1]/2-10
        health_img = self.health_img.copy()

        for heart in range(int(self.health/20)):
            x = self.rect.centerx + heart * health_img.get_size()[0]
            surface.blit(health_img, (x, y))
        if self.health >= 0:
            hp = pygame.font.SysFont(None, 15).render(str(self.health), True, (0, 0, 0))
            surface.blit(hp, (self.rect.centerx, y-10))

    def update(self, surface: Surface, walls: Group(), dt: int):

        self.walls = walls

        keys = pygame.key.get_pressed()
        if keys[self.control.left]:
            self.move(Direction.LEFT)
        if keys[self.control.right]:
            self.move(Direction.RIGHT)
        if keys[self.control.up]:
            self.move(Direction.TOP)
        if keys[self.control.down]:
            self.move(Direction.BOTTOM)
        if keys[self.control.fire]:
            now = pygame.time.get_ticks()
            if now - self.last_shot >= self.weapon.rate:
                self.last_shot = now
                self.weapon.fire(self.rect.centerx, self.rect.centery, self.direction)

        self.weapon.bullets.update(dt)
        self.weapon.bullets.draw(surface)

        self.update_hearts(surface)

        hits = self.weapon.get_hits(self.enemie)
        for hit in hits:
            hit.kill()
            self.enemie.damage(self.weapon.damages)

        # pygame.draw.rect(self.image, (int(self.health / float(100) * 100), 50, 50), self.image.get_rect(), True)

        # hits = pygame.sprite.spritecollide(self.enemie, self.weapon.bullets, False)
        # for enemy, bullets in hits:
        #    for bullet in bullets:
        #        enemy.health -= bullet.damage

        surface.blit(self.image, self.rect)

    def damage(self, dmg: int):
        self.health -= dmg
        if self.health < 0:
            self.health = 0

    def move(self, direction: Direction):
        self.direction = direction

        next_x = self.rect.x
        next_y = self.rect.y

        self.rect.x += direction.value[0]*self.velocity
        self.rect.y += direction.value[1]*self.velocity

        hit_box = pygame.sprite.Sprite()
        hit_box.rect = pygame.Rect(self.rect.x, self.rect.y, self.image.get_size()[0], self.image.get_size()[1])

        for wall in self.walls.sprites():
            hit = pygame.sprite.collide_rect(hit_box, wall)
            if hit:
                print("Hit")
                self.rect.x = next_x
                self.rect.y = next_y
                return

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH-self.image.get_size()[0]:
            self.rect.x = WIDTH-self.image.get_size()[0]
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > HEIGHT-self.image.get_size()[1]:
            self.rect.y = HEIGHT-self.image.get_size()[1]

        if direction == Direction.TOP:
            self.image = image.load(self.perso.value[3][0])
        elif direction == Direction.BOTTOM:
            self.image = image.load(self.perso.value[0][0])
        elif direction == Direction.LEFT:
            self.image = image.load(self.perso.value[2][0])
        elif direction == Direction.RIGHT:
            self.image = image.load(self.perso.value[1][0])

    def set_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def add_flask(self, flask: Flask):
        self.flasks.append(flask)

    def add_consumable(self, consumable: Consumable):
        self.consumables.append(consumable)

    def use_flask(self):
        for i in self.flasks:
            flask: Flask = self.flasks[i]
            self.velocity += flask.velocity
            self.health += flask.health
            self.tiredness += flask.tiredness
            self.flasks.pop(i)

    def eat_consumable(self):
        for i in self.consumables:
            consumable: Consumable = self.consumables[i]
            self.velocity += consumable.velocity
            self.tiredness += consumable.tiredness

            self.consumables.pop(i)
