

import sys

import pygame
from pygame.time import Clock
from pygame.mixer import Sound
from constants.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from core.SceneEnum import SceneEnum
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
        self.current_scene: SceneEnum = SceneEnum.MENU
        self.scenes: dict[SceneEnum, Scene] = {
            SceneEnum.MENU: Menu(self.window, self.clock, self.font_menu, self.selection_highlight_menu_sound, self.selection_menu_sound),
            SceneEnum.MENU_DIFFICULTY: MenuDifficulty(self.window, self.clock, self.font_menu, self.selection_highlight_menu_sound, self.selection_menu_sound),
            SceneEnum.GAME: Game(self.window, self.clock, self.font_game)
        }

    
    def run(self):
        self.music.set_volume(0.0)
        self.music.play(loops=-1)
        while self.running:
            self.window.blit(self.fundo, (0, 0))
            events = pygame.event.get()

            self.scenes[self.current_scene].draw()
            new_scene = self.scenes[self.current_scene].update(events)

            if self.current_scene == SceneEnum.MENU_DIFFICULTY and new_scene == SceneEnum.GAME:
                self.scenes[SceneEnum.GAME]

            if new_scene != self.current_scene and self.current_scene == SceneEnum.GAME:
                self.scenes[self.current_scene].reset()
                    
            if new_scene == SceneEnum.EXIT:
                self.running = False

            self.current_scene = new_scene
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

                