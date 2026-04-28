

import pygame

from constants.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from screens.Game import Game

START = 'JOGAR'
QUIT = 'SAIR'




class Menu:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Chicken Invaders")
        self.SELECTED_COLOR = (255, 0, 0)
        self.UNSELECTED_COLOR = (255, 165, 0)

        self.music = pygame.mixer.Sound('./src/sounds/space_heroes.ogg')
        self.font = pygame.font.SysFont("Arial" , 32 , bold = True)

        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.selected = 1

    def run(self):
        self.music.set_volume(0.2)
        self.music.play(100)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
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
                            Game().run()
                        elif self.selected == 2:
                            self.running = False


            self.window.fill((30, 30, 30))
            self.render_menu()
            pygame.display.flip()
            self.clock.tick(FPS)
                        
        pygame.quit()

    def render_menu(self):
        color_start = self.SELECTED_COLOR if self.selected == 1 else self.UNSELECTED_COLOR
        color_quit = self.SELECTED_COLOR if self.selected == 2 else self.UNSELECTED_COLOR

        surf_start = self.font.render(START, True, color_start)
        surf_quit = self.font.render(QUIT, True, color_quit)
        
        rect_start = surf_start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        rect_quit = surf_quit.get_rect(center=(SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2) + 60))

        self.window.blit(surf_start, rect_start)
        self.window.blit(surf_quit, rect_quit)

