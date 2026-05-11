

import pygame
from pygame.event import Event
from core.constants.constants import Settings, AssetsPaths
from core.enums.SceneEnum import SceneEnum
from core.scenes.Scene import Scene
from pygame import Surface
from pygame.time import Clock
from pygame.mixer import Sound

from core.state.GameState import GAME_STATE


class Victory(Scene):

    def __init__(self, window: Surface, clock: Clock) -> None:
        self.window = window
        self.clock = clock
        self.font_big = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_BIG)
        self.font_medium = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_SMALL)
        self.victory_sound = Sound(AssetsPaths.VICTORY_SOUND)
        self.victory_sound.set_volume(0.5)

    def draw(self) -> None:
        self.__draw_text()

    def __draw_text(self):
        surf_game_over = self.font_big.render("Vitoria! Parabens!", 1, pygame.Color("RED"))
        rect_game_over = surf_game_over.get_rect()
        rect_game_over.center = (Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2)

        surf_score = self.font_medium.render(f"Pontuação: {GAME_STATE.score}", True, pygame.Color("WHITE"))
        rect_score = surf_score.get_rect()
        rect_score.center = (Settings.SCREEN_WIDTH // 2, rect_game_over.bottom + 60)

        surf_info = self.font_small.render("ESC: Sair", True, pygame.Color("GRAY"))
        rect_info = surf_info.get_rect(bottomright=(Settings.SCREEN_WIDTH - 20, Settings.SCREEN_HEIGHT - 20))
        
        self.window.blit(surf_info, rect_info)
        self.window.blit(surf_game_over, rect_game_over)
        self.window.blit(surf_score, rect_score)
    
    def update(self, events: list[Event], dt: float):
        for event in events:
            if event.type == pygame.QUIT:
                GAME_STATE.current_scene = SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.victory_sound.stop()
                    GAME_STATE.current_scene = SceneEnum.MENU
    

    def reset(self) -> None:
        self.victory_sound.play()