

import random
from typing import List

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font
from pygame.sprite import Group
from pygame.event import Event

from constants.constants import DIFFICULTIES, DT_DIVISOR, FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from core.Difficulty import Difficulty
from core.SceneEnum import SceneEnum
from core.entities.Enemy import Enemy
from core.entities.Player import Player
from core.scenes.Scene import Scene
from core.state.GameState import GAME_STATE
from utils.utils import fps_counter

class Game(Scene):
    def __init__(self, window: Surface, clock: Clock, font: Font) -> None:
        self.window = window
        self.clock = clock
        self.font = font

        self.paused = False
        self.direction = 1
        self.player = Player((SCREEN_WIDTH - 100) / 2, SCREEN_HEIGHT - 100)
        self.player_group = Group()
        self.player_bullets = Group()
        self.enemies_bullets = Group()
        self.enemies = Group()
        self.difficulty = DIFFICULTIES[Difficulty.NORMAL]

        self.player_group.add(self.player)
        self.JOGO_PAUSADO_TEXT = self.font.render("JOGO PAUSADO!" , 1, pygame.Color("RED"))

    def draw(self):
        dt = self.clock.tick(FPS) / DT_DIVISOR

        if self.paused:    
            retangulo_texto = self.JOGO_PAUSADO_TEXT.get_rect()
            retangulo_texto.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.player_group.draw(self.window)
            self.player_bullets.draw(self.window)
            self.enemies_bullets.draw(self.window)
            self.enemies.draw(self.window)
            self.window.blit(self.JOGO_PAUSADO_TEXT,  retangulo_texto)
            
        else:
            self.player_group.update(dt)
            self.player_bullets.update(dt)
            self.enemies_bullets.update(dt)
            self.player_group.draw(self.window)
            self.player_bullets.draw(self.window)
            self.enemies_bullets.draw(self.window)
            self.enemies.draw(self.window)
            self.detect_enemy_bullet_collision()
            self.detect_player_bullet_collision()

        fps_counter(self.window, self.clock, self.font)

    
    def detect_enemy_bullet_collision(self):
        hits = pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, False)
        for _, enemy_list in hits.items():
            enemy_list: List[Enemy]
            for enemy in enemy_list:
                enemy.receive_damage()

    def detect_player_bullet_collision(self):
        hits = pygame.sprite.groupcollide(self.enemies_bullets, self.player_group, True, False)
        for _, player in hits.items():
            player: List[Player]
            for p in player:
                p.receive_damage()

    def update(self, events: list[Event]):
        for event in events:
            if event.type == pygame.QUIT:
                return SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    self.player.speed += 20
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                if event.key == pygame.K_ESCAPE:
                    return SceneEnum.MENU
                if event.key == pygame.K_SPACE:
                    self.player.shoot(self.player_bullets)

        self.move_enemies()   
        self.add_enemies()
        self.enemy_shot()
        return SceneEnum.GAME
    
    def add_enemies(self):
        x = 50
        y = -100
        max_y = 50
        if len(self.enemies) == 0:
            for _ in range(GAME_STATE.difficulty.ENEMY_AMOUNT):
                self.enemies.add(Enemy(x, y, max_y, GAME_STATE.difficulty.ENEMY_HEALTH))
                x += 100
                if x > SCREEN_WIDTH - 50:
                    x = 50
                    y += 100
                    max_y += 100
    
    def move_enemies(self):
        has_hit_bord = False
        for enemy in self.enemies:
            enemy: Enemy
            if enemy.rect.y >= enemy.max_y:
                if (enemy.rect.x + enemy.rect.width) >= SCREEN_WIDTH or enemy.rect.x <= 0:
                    has_hit_bord = True
                    break

        if has_hit_bord:
            self.direction *= -1

        for enemy in self.enemies:
            enemy: Enemy
            if enemy.rect.y < enemy.max_y:
                enemy.rect.y += round(GAME_STATE.difficulty.ENEMY_SPEED / 2)
            else:
                enemy.rect.x += GAME_STATE.difficulty.ENEMY_SPEED * self.direction
    

    def enemy_shot(self):
        for enemy in self.enemies:
        # Define a chance (ex: 0.01 é 1% de chance por frame)
            if random.random() < 0.005: 
                enemy.shoot(self.enemies_bullets)
    
    def reset(self):
        self.player = Player((SCREEN_WIDTH - 100) / 2, SCREEN_HEIGHT - 100)
        print(self.player.health)
        self.all_sprites = Group()
        self.bullets = Group()
        self.enemies = Group()

        self.all_sprites.add(self.player)
        # self.enemies.add(Enemy(300, 0))