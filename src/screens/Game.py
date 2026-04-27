

from typing import List

import pygame

from constants.constants import DT_DIVISOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from entities.Enemy import Enemy
from entities.Player import Player
from utils.utils import fps_counter


class Game:

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Chicken Invaders")
        self.music = pygame.mixer.Sound('./src/sounds/space_heroes.ogg')
        self.font = pygame.font.SysFont("Arial" , 18 , bold = True)

        self.running = True
        self.paused = False
        self.player = Player((SCREEN_WIDTH - 100) / 2, SCREEN_HEIGHT - 100)
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.all_sprites.add(self.player)
        self.enemies.add(Enemy(300, 0))
        self.JOGO_PAUSADO_TEXT = self.font.render("JOGO PAUSADO!" , 1, pygame.Color("RED"))

    def run(self):
        self.music.set_volume(0.2)
        self.music.play(100)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F5:
                        self.player.speed += 20
                    if event.key == pygame.K_p:
                        self.paused = not self.paused
                    if event.key == pygame.K_SPACE:
                        self.player.shoot(self.bullets)
            
            dt = self.clock.tick(FPS) / DT_DIVISOR

            self.window.fill((30, 30, 30))

            if self.paused:    
                retangulo_texto = self.JOGO_PAUSADO_TEXT.get_rect()
                retangulo_texto.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                self.window.blit(self.JOGO_PAUSADO_TEXT,  retangulo_texto)
            else:
                self.all_sprites.update(dt)
                self.bullets.update(dt)
                self.all_sprites.draw(self.window)
                self.bullets.draw(self.window)
                self.enemies.draw(self.window)
                hits = pygame.sprite.groupcollide(self.bullets, self.enemies, True, False)
                for _, enemy_list in hits.items():
                    enemy_list: List[Enemy]
                    for enemy in enemy_list:
                        enemy.receive_damage()
                if len(self.enemies) == 0:
                    self.enemies.add(Enemy(100, 0))
                    self.enemies.add(Enemy(300, 0))
                    self.enemies.add(Enemy(500, 0))

            fps_counter(self.window, self.clock, self.font)
            pygame.display.flip()
        pygame.quit()

