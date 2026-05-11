

import random
import time
from typing import List

import pygame
from pygame import Surface
from pygame.time import Clock
from pygame.sprite import Group
from pygame.event import Event
from pygame.mixer import Sound

from core.constants.constants import AssetsPaths, Settings
from core.SceneEnum import SceneEnum
from core.entities.Enemy import Enemy
from core.entities.Player import Player
from core.scenes.Scene import Scene
from core.state.GameState import GAME_STATE
from core.utils.utils import fps_counter


class Game(Scene):
    def __init__(self, window: Surface, clock: Clock) -> None:
        self.window = window
        self.clock = clock
        self.font_big = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_BIG)
        self.font_medium = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_MEDIUM)
        self.font_regular = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_REGULAR)
        self.font_small = pygame.font.Font(AssetsPaths.FONT, Settings.FONT_SIZE_SMALL)
        self.music = Sound(AssetsPaths.SPACE_HEROES)
        self.music.set_volume(0.2)

        self.is_paused = False
        self.direction = 1
        self.enemy_last_shot = -1
        self.last_score = -1
        self.player: Player
        self.player_group = Group()
        self.player_bullets = Group()
        self.enemies_bullets = Group()
        self.enemies = Group()

        self.JOGO_PAUSADO_TEXT = self.font_medium.render("JOGO PAUSADO!" , 1, pygame.Color("RED"))

    def draw(self):
        if self.is_paused:    
            retangulo_texto = self.JOGO_PAUSADO_TEXT.get_rect()
            retangulo_texto.center = (Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT // 2)
            self.window.blit(self.JOGO_PAUSADO_TEXT,  retangulo_texto)

        self.player_group.draw(self.window)
        self.player_bullets.draw(self.window)
        self.enemies_bullets.draw(self.window)
        self.enemies.draw(self.window)

        self.__draw_text()


    def __draw_text(self):
        fps_counter(self.window, self.clock, self.font_small)
        surf_player_health = self.font_regular.render(f"Vida: {self.player.health}", True, pygame.Color("GRAY"))
        rect_player_health = surf_player_health.get_rect(topleft = (0, 20))
        
        surf_info = self.font_small.render("WASD: Mover | ESPAÇO: Atirar | P: Pausar | ESC: Sair", True, pygame.Color("GRAY"))
        rect_info = surf_info.get_rect(bottomright=(Settings.SCREEN_WIDTH - 20, Settings.SCREEN_HEIGHT - 20))
        self.window.blit(surf_info, rect_info)
        self.window.blit(surf_player_health, rect_player_health)

    
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

    def detect_game_over(self):
        if self.player.health <= 0:
            self.music.fadeout(0)
            self.music.stop()
            GAME_STATE.current_scene = SceneEnum.GAME_OVER


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
                    self.music.fadeout(0)
                    self.music.stop()
                    GAME_STATE.current_scene = SceneEnum.MENU

        if not self.is_paused:
            self.player_group.update(dt)
            self.player_bullets.update(dt)
            self.enemies_bullets.update(dt)
            self.detect_game_over()
            self.move_enemies(dt)   
            self.add_enemies()
            self.enemy_shot()
            self.detect_enemy_bullet_collision()
            self.detect_player_bullet_collision()
            self.increase_score_over_time()


    def add_enemies(self):
        if len(self.enemies) != 0:
            return
        
        COLUMNS = 6
        ROWS = GAME_STATE.difficulty.ENEMY_AMOUNT // COLUMNS
        spacing  = Settings.SCREEN_WIDTH // (COLUMNS + 1)
        y = -100
        for _row in range(ROWS):
            for column in range(COLUMNS):
                x = (column + 1) * spacing
                self.enemies.add(Enemy(x, y, target_y=y + 150, health=GAME_STATE.difficulty.ENEMY_HEALTH))
            y += 100



    
    def move_enemies(self, dt: float):
        has_hit_bord = False
        for enemy in self.enemies:
            enemy: Enemy
            if enemy.rect.y >= enemy.target_y:
                if (enemy.rect.x + enemy.rect.width) >= Settings.SCREEN_WIDTH or enemy.rect.x <= 0:
                    has_hit_bord = True
                    break

        if has_hit_bord:
            self.direction *= -1

        for enemy in self.enemies:
            enemy: Enemy
            if enemy.rect.y < enemy.target_y:
                enemy.pos_y += enemy.speed * dt
            else:
                enemy.pos_x += (enemy.speed * dt) * self.direction
            enemy.rect.y = round(enemy.pos_y)
            enemy.rect.x = round(enemy.pos_x)
        
    

    def enemy_shot(self):
        if len(self.enemies) == 0:
            return
        
        now = time.time_ns() // 1_000_000

        if now - self.enemy_last_shot > GAME_STATE.difficulty.ENEMY_FIRE_RATE:
            enemy: Enemy = random.choice(self.enemies.sprites())
            if enemy.rect.y >= enemy.target_y:
                enemy.shoot(self.enemies_bullets)
                self.enemy_last_shot = now

    def increase_score_over_time(self):
        now = time.time_ns() // 1_000_000
        
        if now - self.last_score > 1_000:
            GAME_STATE.increase_score(Settings.SCORE_OVER_TIME)
            self.last_score = now
    
    def reset(self):
        self.is_paused = False
        self.direction = 1
        self.enemy_last_shot = -1
        self.last_score = -1
        self.player = Player(round((Settings.SCREEN_WIDTH - 100) / 2), Settings.SCREEN_HEIGHT - 100)
        self.player_group = Group()
        self.player_bullets = Group()
        self.enemies_bullets = Group()
        self.enemies = Group()
        self.add_enemies()
        self.player_group.add(self.player)
        GAME_STATE.reset()
        self.music.play(loops=-1)