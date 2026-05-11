

import pygame
import time
from pygame.mixer import Sound
from pygame.sprite import Group
from core.constants.constants import Settings, AssetsPaths
from core.entities.PlayerBullet import PlayerBullet
from core.entities.Entity import Entity
from core.state.GameState import GAME_STATE
from pygame.event import Event


class Player(Entity):

    def __init__(self, x: int, y: int):
        super().__init__(x=x, y=y, image_path=AssetsPaths.SPACESHIP, scale_factor=2)
        self.speed = GAME_STATE.difficulty.PLAYER_SPEED
        self.health = GAME_STATE.difficulty.PLAYER_HEALTH
        self.shoot_sound = Sound(AssetsPaths.LASER_SHOOT)
        self.shoot_sound.set_volume(0.5)
        self.last_shot = -1


    def update(self, dt: float) -> None:
        self.move(dt)

    
    def handle_input(self, event: Event, player_bullets: Group):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                now = time.time_ns() // 1_000_000
                if now - self.last_shot > GAME_STATE.difficulty.PLAYER_FIRE_RATE:
                    self.shoot(player_bullets)
                    self.last_shot = now

    def move(self, dt: float):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            self.pos_x -= self.speed * dt

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.rect.x + self.rect.width) < Settings.SCREEN_WIDTH:
            self.pos_x += self.speed * dt

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > 0 and self.rect.y > (Settings.SCREEN_HEIGHT // 2):
            self.pos_y -= self.speed * dt

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.rect.y + self.rect.height < Settings.SCREEN_HEIGHT):
            self.pos_y += self.speed * dt

        self.rect.x = round(self.pos_x)
        self.rect.y = round(self.pos_y)



    def shoot(self, bullets: Group):
        if self.health <= 0:
            return
        
        new_bullet = PlayerBullet(self.rect.centerx, self.rect.top)
        bullets.add(new_bullet)
        self.shoot_sound.play()


    
    def receive_damage(self, amount = 100):
        self.health -= amount
        if self.health <= 0:
            self.kill()
