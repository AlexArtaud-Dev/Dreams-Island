import sys

import pygame

from src.entities.flask import Flask
from src.entities.player.player import Player, Perso, Control
from src.entities.player.weapon import Weapon
from src.settings import *
from src.views.game import Game
from src.views.rules import Rule


class Main(object):
    def __init__(self, name: str, items, bg_color=(0, 0, 0), font=None,
                 font_size=100, font_color=(255, 255, 255)):

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(name)

        self.players = []

        self.flasks = []
        self.weapons = []
        self.protection = []

        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height

        # Background Main Menu
        self.bg_color = bg_color
        self.background = pygame.image.load('./assets/views/entry.png')
        self.background_rect = self.background.get_rect()

        # Sound Menu Change
        # self.menu_sound = pygame.mixer.Sound('resources/sounds/menu_noise.wav')
        # self.valid_menu_sound = pygame.mixer.Sound('resources/sounds/menu_valid_sound.wav')

        # Menu Music
        # self.menu_music = pygame.mixer.music.load('resources/sounds/music.mp3')
        # pygame.mixer.music.set_volume(0.5)

        # Main Menu
        self.font = pygame.font.SysFont(font, font_size)

        self.paddingx = 50
        self.paddingy = 10

        self.start_selected = False
        self.settings_selected = False
        self.quit_select = False

        self.index_selected = 0
        self.current_item = ()
        self.menu_items = []

        # Position menu titles on the menu screen
        for index, item in enumerate(items):
            label = self.font.render(item, True, font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.scr_width / 2) - (width / 2)
            # t_h: total height of text block
            t_h = len(items) * height

            posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
            self.menu_items.append([item, label, (width, height), (posx, posy)])

    def run(self):
        while True:
            # if not pygame.mixer.music.get_busy():
            # pygame.mixer.music.rewind()
            # pygame.mixer.music.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # self.menu_sound.play()
                        for index, item in enumerate(self.menu_items):
                            if self.current_item[0] == item[0]:
                                if self.index_selected > 0:
                                    self.index_selected -= 1
                    if event.key == pygame.K_DOWN:
                        # self.menu_sound.play()
                        for index, item in enumerate(self.menu_items):
                            if self.current_item[0] == item[0]:
                                if self.index_selected < (len(self.menu_items) - 1):
                                    self.index_selected += 1

                    if event.key == pygame.K_RETURN:
                        # self.valid_menu_sound.play()
                        if len(self.current_item) > 0:
                            if self.current_item[0] == "Start":
                                self.play()
                            elif self.current_item[0] == "Settings":
                                pass
                            elif self.current_item[0] == "Règles":
                                        self.play_rule()
                            elif self.current_item[0] == "Quit":
                                pygame.quit()
                                sys.exit()
                            # pygame.mixer.music.fadeout(1000)

            self.current_item = self.menu_items[self.index_selected]

            # Redraw the background
            self.screen.fill(self.bg_color)

            if not self.start_selected or not self.settings_selected:
                self.screen.blit(self.background, self.background_rect)

                for name, label, (width, height), (posx, posy) in self.menu_items:
                    self.screen.blit(label, (posx, posy))

                name, label, (width, height), (posx, posy) = self.current_item

                pygame.draw.rect(
                    self.screen, (255, 255, 255),
                    [
                        posx - self.paddingx, posy - self.paddingy,
                        width + self.paddingx + self.paddingx, height + self.paddingy
                    ], 2)

            pygame.display.flip()

    def play(self):
        weapon1 = Weapon("AK-47", 5, False, 100, 7, 350, "./assets/weapons/pulse1.png")
        flask1 = Flask('name: str', 10, 10, 10, "./assets/weapons/pulse1.png")

        player1 = Player("Kilian", 5, Perso.DEFAULT, 250, 250, Control(P1_LEFT, P1_RIGHT, P1_UP, P1_DOWN, P1_FIRE))
        player2 = Player("Kilian", 5, Perso.DEFAULT, 250, 250, Control(P2_LEFT, P2_RIGHT, P2_UP, P2_DOWN, P2_FIRE))

        player1.set_weapon(weapon1)

        game = Game(player1, player2)
        game.run(self.screen, self.clock)

    def play_rule(self):
        rule = Rule()
        rule.run(self.screen, self.clock)
        for event in pygame.event.get():
            if event.type == pygame.quit():
                sys.exit()
            if event.key == pygame.K_RIGHT:
                rule.run_p2()
                #todo

if True:
    main = Main("Roasted", ['Start', 'Aide','Règles', 'Credits', 'Score', 'Settings', 'Sauvegarder', 'Quit'])
    main.run()

pygame.quit()
