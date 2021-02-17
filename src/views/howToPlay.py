import pygame

from src.settings import WIDTH, HEIGHT, FPS, RULES
from pygame.time import Clock
from pygame.surface import Surface


class HowToPlay:
    def __init__(self):
        self.running = False

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self, surface: Surface, clock: Clock):
        self.running = True
        while self.running:
            self.events()
            self.update(surface)
            dt = clock.tick(FPS)

    def update(self, surface: Surface):
        background = pygame.image.load()

        self.screen.blit(background, (0, 0))
        pygame.display.flip()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
