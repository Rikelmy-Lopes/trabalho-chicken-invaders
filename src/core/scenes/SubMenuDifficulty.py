

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font
from pygame.mixer import Sound
from pygame.sprite import Group
from pygame.event import Event

from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SELECTED_COLOR_MENU, UNSELECTED_COLOR_MENU
from core.State import State


VERY_HARD = 'QUERO GALINHADA (MUITO DIFICIL)'
HARD = 'DIFICIL'
NORMAL = 'NORMAL'
EASY = 'FACIL'


class SubMenuDifficulty:
    SELECTED_COLOR = SELECTED_COLOR_MENU
    UNSELECTED_COLOR = UNSELECTED_COLOR_MENU

    def __init__(self, window: Surface, clock: Clock, font: Font, selection_highlight_menu_sound: Sound, selection_menu_sound: Sound) -> None:
        self.window = window
        self.clock = clock
        self.font = font
        self.selection_highlight_menu_sound = selection_highlight_menu_sound
        self.selection_menu_sound = selection_menu_sound
        self.all_sprites = Group()
        self.selected_difficulty = 3



    def draw_menu(self):
        color_very_hard = self.SELECTED_COLOR if self.selected_difficulty == 1 else self.UNSELECTED_COLOR
        color_hard = self.SELECTED_COLOR if self.selected_difficulty == 2 else self.UNSELECTED_COLOR
        color_normal = self.SELECTED_COLOR if self.selected_difficulty == 3 else self.UNSELECTED_COLOR
        color_easy = self.SELECTED_COLOR if self.selected_difficulty == 4 else self.UNSELECTED_COLOR

        surf_very_hard = self.font.render(VERY_HARD, True, color_very_hard)
        surf_hard = self.font.render(HARD, True, color_hard)
        surf_normal = self.font.render(NORMAL, True, color_normal)
        surf_easy = self.font.render(EASY, True, color_easy)
        
        rect_very_hard = surf_very_hard.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        rect_hard = surf_hard.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 - 60) + 60))
        rect_normal = surf_normal.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 - 60) + 120))
        rect_easy = surf_easy.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 - 60) + 180))

        self.window.blit(surf_very_hard, rect_very_hard)
        self.window.blit(surf_hard, rect_hard)
        self.window.blit(surf_normal, rect_normal)
        self.window.blit(surf_easy, rect_easy)



    def select_menu_difficulty(self, event: Event):
        if event.key == pygame.K_DOWN:
            if self.selected_difficulty == 4:
                self.selected_difficulty = 1
            else:
                self.selected_difficulty += 1
            self.selection_highlight_menu_sound.play()
        if event.key == pygame.K_UP:
            if self.selected_difficulty == 1:
                self.selected_difficulty = 4
            else:
                self.selected_difficulty -= 1
            self.selection_highlight_menu_sound.play()
    
     
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.select_menu_difficulty(event)
                if event.key == pygame.K_RETURN:
                    self.selection_menu_sound.play()
                    return State.GAME
                if event.key == pygame.K_ESCAPE:
                    return State.MENU
        return State.SUBMENU