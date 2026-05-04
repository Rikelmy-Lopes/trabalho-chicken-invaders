

import sys

import pygame
from pygame.time import Clock
from pygame.mixer import Sound
from constants.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from core.State import State
from core.scenes.Game import Game
from core.scenes.Menu import Menu
from core.scenes.MenuDifficulty import MenuDifficulty
from core.scenes.Scene import Scene


class Engine:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Chicken Invaders")

        self.music = Sound('./src/sounds/space_heroes.ogg')
        self.selection_highlight_menu_sound = Sound('./src/sounds/vgmenuhighlight.ogg')
        self.selection_menu_sound = Sound('./src/sounds/menu_selection.wav')
        self.font_menu = pygame.font.SysFont("Arial" , 32, bold = True)
        self.font_game = pygame.font.SysFont("Arial" , 18 , bold = True)
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = Clock()
        self.fundo = pygame.image.load('./src/images/space.png').convert()
        self.fundo = pygame.transform.scale(self.fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.state: State = State.MENU
        self.scenes: dict[State, Scene] = {
            State.MENU: Menu(self.window, self.clock, self.font_menu, self.selection_highlight_menu_sound, self.selection_menu_sound),
            State.SUBMENU: MenuDifficulty(self.window, self.clock, self.font_menu, self.selection_highlight_menu_sound, self.selection_menu_sound),
            State.GAME: Game(self.window, self.clock, self.font_game)
        }

    
    def run(self):
        self.music.set_volume(0.1)
        self.music.play(loops=-1)
        while self.running:
            self.window.blit(self.fundo, (0, 0))
            events = pygame.event.get()

            self.scenes[self.state].draw()
            self.state = self.scenes[self.state].update(events)

            if self.state == State.MENU:
                if self.scenes[State.GAME] is not None:
                    self.scenes[State.GAME].reset()
            elif self.state == State.EXIT:
                self.running = False
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

                