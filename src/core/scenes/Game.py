

from typing import List

import pygame

from constants.constants import DT_DIVISOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from core.entities.Enemy import Enemy
from core.entities.Player import Player
from utils.utils import fps_counter


class Game:
    def __init__(self, window: pygame.Surface, clock: pygame.time.Clock, font: pygame.font.Font) -> None:
        self.window = window
        self.clock = clock
        self.font = font

        self.running = True
        self.paused = False
        self.player = Player((SCREEN_WIDTH - 100) / 2, SCREEN_HEIGHT - 100)
        self.all_sprites = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.all_sprites.add(self.player)
        self.enemies.add(Enemy(300, 0))
        self.JOGO_PAUSADO_TEXT = self.font.render("JOGO PAUSADO!" , 1, pygame.Color("RED"))

    def draw(self):
        dt = self.clock.tick(FPS) / DT_DIVISOR

        if self.paused:    
            retangulo_texto = self.JOGO_PAUSADO_TEXT.get_rect()
            retangulo_texto.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.all_sprites.draw(self.window)
            self.bullets.draw(self.window)
            self.enemies.draw(self.window)
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

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "EXIT"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    self.player.speed += 20
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                if event.key == pygame.K_ESCAPE:
                    return "MENU"
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self.bullets)
        return "GAME"