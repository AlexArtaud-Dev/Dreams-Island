from sys import path

import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.time import Clock

from src.entities.player.player import Player
from src.entities.vegetations.three import Three
from src.entities.wall import Wall
from src.settings import *


class Game(object):
    def __init__(self, player1: Player, player2: Player):
        self.running = False

        self.days = 10

        self.background = pygame.image.load(BACKGROUND_NIGHT).convert()

        self.players = Group()
        self.players.add(player1)
        self.players.add(player2)

        player1.set_enemie(player2)
        player2.set_enemie(player1)

        self.map = []

        self.walls = Group()

        self.threes = Group()
        self.bushes = Group()

    def run(self, surface: Surface, clock: Clock):
        self.running = True
        self.load_map()

        dt = 0
        while self.running:
            self.events()
            self.update(surface, dt)
            dt = clock.tick(FPS)

    def update(self, surface: Surface, dt: int):
        surface.fill((250, 250, 250))
        layout = pygame.image.load(OVERLAY).convert_alpha()

        background = self.background.copy()

        self.players.update(background, self.walls, dt)

        pi = 0
        for player in self.players:
            camerax = player.rect.centerx * 2 - WIDTH / 4
            cameray = player.rect.centery * 2 - HEIGHT / 2
            layout_pos = (camerax, cameray)

            if camerax < 0:
                camerax = 0
            elif camerax > WIDTH * 2 - WIDTH / 2:
                camerax = WIDTH * 2 - WIDTH / 2

            if cameray < 0:
                cameray = 0
            elif cameray > HEIGHT:
                cameray = HEIGHT

            camera_rect = pygame.Rect(camerax, cameray, WIDTH / 2, HEIGHT)

            camera_view = pygame.transform.scale2x(background).subsurface(camera_rect)
            # camera_view.blit(layout, layout_pos)

            surface.blit(camera_view, (WIDTH * pi / 2, 0))
            pi += 1

        pygame.display.flip()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False

    def load_map(self):
        with open("./assets/map.txt", "rt") as f:
            for line in f:
                self.map.append(line)

        self.init_walls()
        self.init_threes()

    def init_walls(self):
        for row, tiles in enumerate(self.map):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.walls.add(Wall(col, row))

    def init_threes(self):
        group = pygame.sprite.LayeredUpdates()
        for row, tiles in enumerate(self.map):
            for col, tile in enumerate(tiles):
                if tile == 'T':
                    group.add(Three(col, row, THREE1))
        group.draw(self.background)
