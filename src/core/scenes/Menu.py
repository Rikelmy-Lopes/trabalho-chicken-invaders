

import pygame

from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH

START = 'JOGAR'
QUIT = 'SAIR'


VERY_HARD = 'QUERO GALINHADA (MUITO DIFICIL)'
HARD = 'DIFICIL'
NORMAL = 'NORMAL'
EASY = 'FACIL'

class Menu:
    SELECTED_COLOR = (255, 0, 0)
    UNSELECTED_COLOR = (255, 165, 0)

    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font) -> None:
        self.window = window
        self.clock = clock
        self.font = font
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.selection_highlight_menu_sound = pygame.mixer.Sound('./src/sounds/vgmenuhighlight.ogg')
        self.selection_menu_sound = pygame.mixer.Sound('./src/sounds/menu_selection.wav')
        self.fundo = pygame.image.load('./src/images/space.png').convert()
        self.fundo = pygame.transform.scale(self.fundo, (SCREEN_WIDTH, SCREEN_HEIGHT))


        self.selected = 1
        self.selected_difficulty = None

    def draw(self):
        self.window.blit(self.fundo, (0, 0))
        if self.selected == 1 and self.selected_difficulty is not None:
            self.__draw_menu_difficulty()
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

    def __draw_menu_difficulty(self):
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


    def update(self) -> str:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                self.select_menu(event)
                self.select_menu_difficulty(event)
                if event.key == pygame.K_RETURN:
                    if self.selected == 1 and self.selected_difficulty is None:
                        self.selected_difficulty = 3
                    elif self.selected == 2:
                        return "EXIT"
                    self.selection_menu_sound.play()
                if event.key == pygame.K_ESCAPE and self.selected_difficulty is not None:
                    self.selected_difficulty = None
                    self.selection_menu_sound.play()
                    
        return "MENU"
    
    def select_menu(self, event: pygame.event.Event):
        if event.key == pygame.K_DOWN and self.selected_difficulty is None:
            if self.selected == 2:
                self.selected = 1
            else:
                self.selected += 1
            self.selection_highlight_menu_sound.play()
        if event.key == pygame.K_UP and self.selected_difficulty is None:
            if self.selected == 1:
                self.selected = 2
            else:
                self.selected -= 1
            self.selection_highlight_menu_sound.play()

    def select_menu_difficulty(self, event: pygame.event.Event):
        if event.key == pygame.K_DOWN and self.selected_difficulty is not None:
            if self.selected_difficulty == 4:
                self.selected_difficulty = 1
            else:
                self.selected_difficulty += 1
            self.selection_highlight_menu_sound.play()
        if event.key == pygame.K_UP and self.selected_difficulty is not None:
            if self.selected_difficulty == 1:
                self.selected_difficulty = 4
            else:
                self.selected_difficulty -= 1
            self.selection_highlight_menu_sound.play()