import pygame

from src.settings import WIDTH, HEIGHT, FPS, RULES_P1, RULES_P2
from pygame.time import Clock
from pygame.surface import Surface


class Rule:
    def __init__(self):
        self.running = False

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self, surface: Surface, clock: Clock):
        self.running = True
        while self.running:
            self.events()
            self.update(surface)
            clock.tick(FPS)

    def run_p2(self, surface: Surface, clock: Clock):
        self.running = True
        while self.running:
            self.events()
            self.update_p2(surface)
            clock.tick(FPS)

    def update(self, surface: Surface):
        background = pygame.image.load(RULES_P1)

        self.screen.blit(background, (0, 0))
        pygame.display.flip()

    def update_p2(self, surface: Surface):
        background = pygame.image.load(RULES_P1)
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
