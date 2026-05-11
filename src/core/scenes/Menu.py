

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.mixer import Sound
from pygame.sprite import Group
from pygame.event import Event

from core.constants.constants import Settings, AssetsPaths
from core.enums.SceneEnum import SceneEnum
from core.scenes.Scene import Scene
from core.state.GameState import GAME_STATE

TITLE = 'CHICKEN INVADERS'
START = 'JOGAR'
QUIT = 'SAIR'


class Menu(Scene):

    def __init__(self, window: Surface, clock: Clock, selection_highlight_menu_sound: Sound, selection_menu_sound: Sound) -> None:
        self.window = window
        self.clock = clock
        self.font_big = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_BIG)
        self.font_medium = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_MEDIUM)
        self.font_small = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_SMALL)
        self.all_sprites = Group()
        self.selection_highlight_menu_sound = selection_highlight_menu_sound
        self.selection_menu_sound = selection_menu_sound

        self.selected = 1

    def draw(self):
        self.__draw_text()

    def __draw_text(self):
        color_start = Settings.SELECTED_COLOR_MENU if self.selected == 1 else Settings.UNSELECTED_COLOR_MENU
        color_quit = Settings.SELECTED_COLOR_MENU if self.selected == 2 else Settings.UNSELECTED_COLOR_MENU

        surf_title = self.font_big.render(TITLE, True, pygame.Color("RED"))
        surf_start = self.font_medium.render(START, True, color_start)
        surf_quit = self.font_medium.render(QUIT, True, color_quit)
        surf_info = self.font_small.render("Cima/Baixo: Mover | Enter: Selecionar", True, pygame.Color("GRAY"))
        
        
        rect_title = surf_title.get_rect(center=(Settings.SCREEN_WIDTH // 2, (Settings.SCREEN_HEIGHT // 2) - 100))
        rect_start = surf_start.get_rect(center=(Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2))
        rect_quit = surf_quit.get_rect(center=(Settings.SCREEN_WIDTH // 2, (Settings.SCREEN_HEIGHT // 2) + 60))
        rect_info = surf_info.get_rect(bottomright=(Settings.SCREEN_WIDTH - 20, Settings.SCREEN_HEIGHT - 20))

        self.window.blit(surf_title, rect_title)
        self.window.blit(surf_start, rect_start)
        self.window.blit(surf_quit, rect_quit)
        self.window.blit(surf_info, rect_info)

    def update(self, events: list[Event], dt: float):
        for event in events:
            if event.type == pygame.QUIT:
                GAME_STATE.current_scene = SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                self.move_selection(event)
                if event.key == pygame.K_RETURN:
                    if self.selected == 1:
                        self.selection_menu_sound.play()
                        GAME_STATE.current_scene = SceneEnum.MENU_DIFFICULTY
                    elif self.selected == 2:
                        self.selection_menu_sound.play()
                        GAME_STATE.current_scene = SceneEnum.EXIT
    
    def move_selection(self, event: Event):
        if event.key == pygame.K_DOWN:
            if self.selected == 2:
                self.selected = 1
            else:
                self.selected += 1
            self.selection_highlight_menu_sound.play()
        if event.key == pygame.K_UP:
            if self.selected == 1:
                self.selected = 2
            else:
                self.selected -= 1
            self.selection_highlight_menu_sound.play()

    def reset(self) -> None:
        pass