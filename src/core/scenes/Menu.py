

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font
from pygame.mixer import Sound
from pygame.sprite import Group
from pygame.event import Event

from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SELECTED_COLOR_MENU, UNSELECTED_COLOR_MENU
from core.State import State

START = 'JOGAR'
QUIT = 'SAIR'

class Menu:
    SELECTED_COLOR = SELECTED_COLOR_MENU
    UNSELECTED_COLOR = UNSELECTED_COLOR_MENU

    def __init__(self, window: Surface, clock: Clock, font: Font, selection_highlight_menu_sound: Sound, selection_menu_sound: Sound) -> None:
        self.window = window
        self.clock = clock
        self.font = font
        self.all_sprites = Group()
        self.selection_highlight_menu_sound = selection_highlight_menu_sound
        self.selection_menu_sound = selection_menu_sound

        self.selected = 1

    def draw(self):
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

    def update(self, events: list[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                return State.EXIT
            if event.type == pygame.KEYDOWN:
                self.select_menu(event)
                if event.key == pygame.K_RETURN:
                    if self.selected == 1:
                        return State.SUBMENU
                    elif self.selected == 2:
                        return State.EXIT
                    self.selection_menu_sound.play()
        return State.MENU
    
    def select_menu(self, event: Event):
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