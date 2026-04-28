

import pygame

from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH

START = 'JOGAR'
QUIT = 'SAIR'




class Menu:
    SELECTED_COLOR = (255, 0, 0)
    UNSELECTED_COLOR = (255, 165, 0)

    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font) -> None:
        self.window = window
        self.clock = clock
        self.font = font
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        self.selected = 1

    def draw(self):
        self.window.fill((30, 30, 30))
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
                if event.key == pygame.K_DOWN:
                    if self.selected == 2:
                        self.selected = 1
                    else:
                        self.selected += 1
                if event.key == pygame.K_UP:
                    if self.selected == 1:
                        self.selected = 2
                    else:
                        self.selected -= 1
                if event.key == pygame.K_RETURN:
                    if self.selected == 1:
                        return "GAME"
                    elif self.selected == 2:
                        return "EXIT"
        return "MENU"