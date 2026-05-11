

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.mixer import Sound
from pygame.sprite import Group
from pygame.event import Event

from core.constants.constants import Settings, AssetsPaths
from core.Difficulty import Difficulty
from core.SceneEnum import SceneEnum
from core.scenes.Scene import Scene
from core.state.GameState import GAME_STATE

TITLE = 'ESCOLHA A DIFICULDADE'
VERY_HARD = 'QUERO GALINHADA (MUITO DIFICIL)'
HARD = 'DIFICIL'
NORMAL = 'NORMAL'
EASY = 'FACIL'


class MenuDifficulty(Scene):

    def __init__(self, window: Surface, clock: Clock, selection_highlight_menu_sound: Sound, selection_menu_sound: Sound) -> None:
        self.window = window
        self.clock = clock
        self.font_big = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_BIG)
        self.font_medium = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_SMALL)
        self.selection_highlight_menu_sound = selection_highlight_menu_sound
        self.selection_menu_sound = selection_menu_sound
        self.all_sprites = Group()
        self.selected_difficulty = GAME_STATE.difficulty.difficulty_value.value


    def draw(self) -> None:
        self.__draw_text()

    def __draw_text(self):
        color_very_hard = Settings.SELECTED_COLOR_MENU if self.selected_difficulty == 4 else Settings.UNSELECTED_COLOR_MENU
        color_hard = Settings.SELECTED_COLOR_MENU if self.selected_difficulty == 3 else Settings.UNSELECTED_COLOR_MENU
        color_normal = Settings.SELECTED_COLOR_MENU if self.selected_difficulty == 2 else Settings.UNSELECTED_COLOR_MENU
        color_easy = Settings.SELECTED_COLOR_MENU if self.selected_difficulty == 1 else Settings.UNSELECTED_COLOR_MENU

        surf_title = self.font_big.render(TITLE, True, pygame.Color("RED"))
        surf_info = self.font_small.render("Cima/Baixo: Mover | Enter: Selecionar | ESC: Voltar", True, pygame.Color("GRAY"))
        surf_very_hard = self.font_medium.render(VERY_HARD, True, color_very_hard)
        surf_hard = self.font_medium.render(HARD, True, color_hard)
        surf_normal = self.font_medium.render(NORMAL, True, color_normal)
        surf_easy = self.font_medium.render(EASY, True, color_easy)
        
        rect_title = surf_title.get_rect(center=(Settings.SCREEN_WIDTH // 2, (Settings.SCREEN_HEIGHT // 2) - 150))
        rect_info = surf_info.get_rect(bottomright=(Settings.SCREEN_WIDTH - 20, Settings.SCREEN_HEIGHT - 20))
        rect_very_hard = surf_very_hard.get_rect(center=(Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2 - 60))
        rect_hard = surf_hard.get_rect(center=(Settings.SCREEN_WIDTH // 2, (Settings.SCREEN_HEIGHT // 2 - 60) + 60))
        rect_normal = surf_normal.get_rect(center=(Settings.SCREEN_WIDTH // 2, (Settings.SCREEN_HEIGHT // 2 - 60) + 120))
        rect_easy = surf_easy.get_rect(center=(Settings.SCREEN_WIDTH // 2, (Settings.SCREEN_HEIGHT // 2 - 60) + 180))

        self.window.blit(surf_title, rect_title)
        self.window.blit(surf_very_hard, rect_very_hard)
        self.window.blit(surf_hard, rect_hard)
        self.window.blit(surf_normal, rect_normal)
        self.window.blit(surf_easy, rect_easy)
        self.window.blit(surf_info, rect_info)



    def move_selection(self, event: Event):
        if event.key == pygame.K_DOWN:
            if self.selected_difficulty == 1:
                self.selected_difficulty = 4
            else:
                self.selected_difficulty -= 1
            self.selection_highlight_menu_sound.play()
        if event.key == pygame.K_UP:
            if self.selected_difficulty == 4:
                self.selected_difficulty = 1
            else:
                self.selected_difficulty += 1
            self.selection_highlight_menu_sound.play()
    
     
    def update(self, events: list[Event], dt: float):
        for event in events:
            if event.type == pygame.QUIT:
                GAME_STATE.current_scene = SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                self.move_selection(event)
                if event.key == pygame.K_RETURN:
                    self.selection_menu_sound.play()
                    GAME_STATE.update_difficulty(Difficulty(self.selected_difficulty))
                    GAME_STATE.current_scene = SceneEnum.GAME
                if event.key == pygame.K_ESCAPE:
                    self.selection_menu_sound.play()
                    GAME_STATE.current_scene = SceneEnum.MENU
    

    def reset(self) -> None:
        pass