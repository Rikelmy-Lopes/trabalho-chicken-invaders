

import random
import time
from typing import List

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.font import Font
from pygame.sprite import Group
from pygame.event import Event

from constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH
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

        self.is_paused = False
        self.direction = 1
        self.player: Player
        self.player_group = Group()
        self.player_bullets = Group()
        self.enemies_bullets = Group()
        self.enemies = Group()
        self.difficulty = GAME_STATE.difficulty
        self.last_shot = -1

        self.JOGO_PAUSADO_TEXT = self.font.render("JOGO PAUSADO!" , 1, pygame.Color("RED"))

    def draw(self):
        if self.is_paused:    
            retangulo_texto = self.JOGO_PAUSADO_TEXT.get_rect()
            retangulo_texto.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            self.window.blit(self.JOGO_PAUSADO_TEXT,  retangulo_texto)

        self.player_group.draw(self.window)
        self.player_bullets.draw(self.window)
        self.enemies_bullets.draw(self.window)
        self.enemies.draw(self.window)

        fps_counter(self.window, self.clock, self.font)

    
    def detect_enemy_bullet_collision(self):
        hits = pygame.sprite.groupcollide(self.player_bullets, self.enemies, True, False)
        for _, enemy_list in hits.items():
            enemy_list: List[Enemy]
            for enemy in enemy_list:
                enemy.receive_damage()

    def detect_player_bullet_collision(self):
        hits = pygame.sprite.groupcollide(self.player_group, self.enemies_bullets, False, True)
        
        if hits:
            self.player.receive_damage()

    def update(self, events: list[Event], dt: float):
        for event in events:
            self.player.handle_input(event, self.player_bullets)
            if event.type == pygame.QUIT:
                GAME_STATE.current_scene = SceneEnum.EXIT
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    self.player.speed += 20
                if event.key == pygame.K_p:
                    self.is_paused = not self.is_paused
                if event.key == pygame.K_ESCAPE:
                    GAME_STATE.current_scene = SceneEnum.MENU

        if self.player.health <= 0:
            GAME_STATE.current_scene = SceneEnum.GAME_OVER

        if not self.is_paused:
            self.player_group.update(dt)
            self.player_bullets.update(dt)
            self.enemies_bullets.update(dt)
            self.move_enemies(dt)   
            self.add_enemies()
            self.enemy_shot()
            self.detect_enemy_bullet_collision()
            self.detect_player_bullet_collision()
    
    def add_enemies(self):
        if len(self.enemies) != 0:
            return
        x = 50
        y = -100
        max_y = 50
        for _ in range(GAME_STATE.difficulty.ENEMY_AMOUNT): 
            self.enemies.add(Enemy(x, y, max_y, GAME_STATE.difficulty.ENEMY_HEALTH))
            x += 100
            if x > SCREEN_WIDTH - 50:
                x = 50
                y += 100
                max_y += 100
    
    def move_enemies(self, dt: float):
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
                enemy.pos_y += (enemy.speed * dt) / 2
            else:
                enemy.pos_x += (enemy.speed * dt) * self.direction
            enemy.rect.y = round(enemy.pos_y)
            enemy.rect.x = round(enemy.pos_x)
        
    

    def enemy_shot(self):
        if len(self.enemies) == 0:
            return
        
        now = time.time_ns() // 1_000_000

        if now - self.last_shot > GAME_STATE.difficulty.ENEMY_BULLET_DELAY:
            enemy: Enemy = random.choice(self.enemies.sprites())
            if enemy.rect.y >= enemy.max_y:
                enemy.shoot(self.enemies_bullets)
                self.last_shot = now
    
    def reset(self):
        self.player = Player(round((SCREEN_WIDTH - 100) / 2), SCREEN_HEIGHT - 100)
        self.player_group = Group()
        self.player_bullets = Group()
        self.enemies_bullets = Group()
        self.enemies = Group()

        self.add_enemies()

        self.player_group.add(self.player)