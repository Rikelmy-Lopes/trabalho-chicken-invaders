

import pygame
from pygame.event import Event
from constants.constants import FONT_PATH, FONT_SIZE_BIG, FONT_SIZE_MEDIUM, FONT_SIZE_SMALL, SCREEN_HEIGHT, SCREEN_WIDTH
from core.SceneEnum import SceneEnum
from core.scenes.Scene import Scene
from pygame import Surface
from pygame.time import Clock

from core.state.GameState import GAME_STATE


class GameOver(Scene):

    def __init__(self, window: Surface, clock: Clock) -> None:
        self.window = window
        self.clock = clock
        self.font_big = pygame.font.Font(FONT_PATH, FONT_SIZE_BIG)
        self.font_medium = pygame.font.Font(FONT_PATH, FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(FONT_PATH, FONT_SIZE_SMALL)

    def draw(self) -> None:
        self.__draw_text()

    def __draw_text(self):
        surf_game_over = self.font_big.render("GAME OVER! Voçê Morreu!" , 1, pygame.Color("RED"))
        rect_game_over = surf_game_over.get_rect()
        rect_game_over.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        surf_info = self.font_small.render("ESC: Sair", True, pygame.Color("GRAY"))
        rect_info = surf_info.get_rect(bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20))
        
        self.window.blit(surf_info, rect_info)
        self.window.blit(surf_game_over, rect_game_over)
    
    def update(self, events: list[Event], dt: float):
        for event in events:
            if event.type == pygame.QUIT:
                GAME_STATE.current_scene = SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    GAME_STATE.current_scene = SceneEnum.MENU
    

    def reset(self) -> None:
        pass