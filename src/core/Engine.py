

import sys

import pygame
from pygame.time import Clock
from pygame.mixer import Sound
from constants.constants import DT_DIVISOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from core.SceneEnum import SceneEnum
from core.scenes.Game import Game
from core.scenes.GameOver import GameOver
from core.scenes.Menu import Menu
from core.scenes.MenuDifficulty import MenuDifficulty
from core.scenes.Scene import Scene
from core.state.GameState import GAME_STATE


class Engine:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Chicken Invaders")

        self.music = Sound('./src/sounds/space_heroes.ogg')
        self.selection_highlight_menu_sound = Sound('./src/sounds/vgmenuhighlight.ogg')
        self.selection_menu_sound = Sound('./src/sounds/menu_selection.wav')
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = Clock()
        self.fundo = pygame.image.load('./src/images/space.png').convert()
        self.fundo = pygame.transform.scale(self.fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.current_scene: SceneEnum = SceneEnum.MENU
        self.scenes: dict[SceneEnum, Scene] = {
            SceneEnum.MENU: Menu(self.window, self.clock, self.selection_highlight_menu_sound, self.selection_menu_sound),
            SceneEnum.MENU_DIFFICULTY: MenuDifficulty(self.window, self.clock, self.selection_highlight_menu_sound, self.selection_menu_sound),
            SceneEnum.GAME: Game(self.window, self.clock),
            SceneEnum.GAME_OVER: GameOver(self.window, self.clock)
        }

    
    def run(self):
        self.music.set_volume(0.0)
        self.music.play(loops=-1)
        while self.running:
            self.window.blit(self.fundo, (0, 0))
            events = pygame.event.get()
            dt = self.clock.tick(FPS) / DT_DIVISOR

            if self.current_scene != GAME_STATE.current_scene:
                if GAME_STATE.current_scene == SceneEnum.GAME:
                    self.scenes[SceneEnum.GAME].reset()

                self.current_scene = GAME_STATE.current_scene

            self.scenes[GAME_STATE.current_scene].draw()
            self.scenes[GAME_STATE.current_scene].update(events, dt)
                    
            if GAME_STATE.current_scene == SceneEnum.EXIT:
                self.running = False
            
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()

                