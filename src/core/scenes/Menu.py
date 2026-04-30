

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font
from pygame.mixer import Sound
from pygame.sprite import Group
from pygame.event import Event

from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SELECTED_COLOR_MENU, UNSELECTED_COLOR_MENU
from core.scenes.SubMenuDifficulty import SubMenuDifficulty

START = 'JOGAR'
QUIT = 'SAIR'

class Menu:
    SELECTED_COLOR = SELECTED_COLOR_MENU
    UNSELECTED_COLOR = UNSELECTED_COLOR_MENU

    def __init__(self, window: Surface, clock: Clock, font: Font) -> None:
        self.window = window
        self.clock = clock
        self.font = font
        self.all_sprites = Group()
        self.selection_highlight_menu_sound = Sound('./src/sounds/vgmenuhighlight.ogg')
        self.selection_menu_sound = Sound('./src/sounds/menu_selection.wav')
        self.sub_menu_difficulty = SubMenuDifficulty(window, clock, font, self.selection_highlight_menu_sound, self.selection_menu_sound)

        self.selected = 1

    def draw(self):
        if self.selected == 1 and self.sub_menu_difficulty.selected_difficulty is not None:
            self.sub_menu_difficulty.draw_menu()
        else:
            self.__draw_menu()

    def __draw_menu(self):
        color_start = self.SELECTED_COLOR if self.selected == 1 else self.UNSELECTED_COLOR
        color_quit = self.SELECTED_COLOR if self.selected == 2 else self.UNSELECTED_COLOR

        surf_start = self.font.render(START, True, color_start)
        surf_quit = self.font.render(QUIT, True, color_quit)
        
        rect_start = surf_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        rect_quit = surf_quit.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 60))

        self.window.blit(surf_start, rect_start)
        self.window.blit(surf_quit, rect_quit)

    def update(self) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                self.select_menu(event)
                self.sub_menu_difficulty.select_menu_difficulty(event)
                if event.key == pygame.K_RETURN:
                    if self.selected == 1 and self.sub_menu_difficulty.selected_difficulty is None:
                        self.sub_menu_difficulty.selected_difficulty = 3
                    elif self.selected == 1 and self.sub_menu_difficulty.selected_difficulty is not None:
                        return "GAME"
                    elif self.selected == 2:
                        return "EXIT"
                    self.selection_menu_sound.play()
                if event.key == pygame.K_ESCAPE and self.sub_menu_difficulty.selected_difficulty is not None:
                    self.sub_menu_difficulty.selected_difficulty = None
                    self.selection_menu_sound.play()
                    
        return "MENU"
    
    def select_menu(self, event: Event):
        if event.key == pygame.K_DOWN and self.sub_menu_difficulty.selected_difficulty is None:
            if self.selected == 2:
                self.selected = 1
            else:
                self.selected += 1
            self.selection_highlight_menu_sound.play()
        if event.key == pygame.K_UP and self.sub_menu_difficulty.selected_difficulty is None:
            if self.selected == 1:
                self.selected = 2
            else:
                self.selected -= 1
            self.selection_highlight_menu_sound.play()