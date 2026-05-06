

import pygame
from pygame.event import Event
from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH
from core.SceneEnum import SceneEnum
from core.scenes.Scene import Scene
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font

from core.state.GameState import GAME_STATE


class GameOver(Scene):

    def __init__(self, window: Surface, clock: Clock, font: Font) -> None:
        self.window = window
        self.clock = clock
        self.font = font
        self.GAME_OVER_TEXT = self.font.render("GAME OVER! Voçê Morreu!" , 1, pygame.Color("RED"))

    def draw(self) -> None:
        retangulo_texto = self.GAME_OVER_TEXT.get_rect()
        retangulo_texto.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.window.blit(self.GAME_OVER_TEXT,  retangulo_texto)
    
    def update(self, events: list[Event], dt: float):
        for event in events:
            if event.type == pygame.QUIT:
                GAME_STATE.current_scene = SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GAME_STATE.current_scene = SceneEnum.MENU
    

    def reset(self) -> None:
        pass