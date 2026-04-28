

import sys

import pygame

from constants.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from core.scenes.Game import Game
from core.scenes.Menu import Menu


class Engine:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Chicken Invaders")

        self.music = pygame.mixer.Sound('./src/sounds/space_heroes.ogg')
        self.font_menu = pygame.font.SysFont("Arial" , 32, bold = True)
        self.font_game = pygame.font.SysFont("Arial" , 18 , bold = True)
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.fundo = pygame.image.load('./src/images/space.png').convert()
        self.fundo = pygame.transform.scale(self.fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.running = True
        self.state = "MENU"
        self.menu = Menu(self.window, self.clock, self.font_menu)
        self.game = None

    
    def run(self):
        self.music.set_volume(0.1)
        self.music.play(loops=-1)
        while self.running:
            self.window.blit(self.fundo, (0, 0))
            if self.state == "MENU":
                if self.game is not None:
                    self.menu.selected_difficulty = None
                    self.game = None
                self.state = self.menu.update()
                self.menu.draw()
            elif self.state == "GAME":
                if self.game is None:
                    self.game = Game(self.window, self.clock, self.font_game)
                self.state = self.game.update()
                self.game.draw()
            elif self.state == "EXIT":
                self.running = False
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

                