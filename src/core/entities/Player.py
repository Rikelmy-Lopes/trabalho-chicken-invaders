

import pygame
from pygame.mixer import Sound
from pygame.sprite import Group
from core.constants.constants import SCREEN_HEIGHT, SCREEN_WIDTH, AssetsPaths
from core.entities.Bullet import Bullet
from core.entities.Entity import Entity
from core.state.GameState import GAME_STATE
from pygame.event import Event

BLUE_COLOR = (0, 0, 255)



class Player(Entity):
    PLAYER_WIDTH = 100
    PLAYER_HEIGHT = 100

    def __init__(self, x: int, y: int):
        super().__init__(x, y, BLUE_COLOR, (self.PLAYER_WIDTH, self.PLAYER_HEIGHT), AssetsPaths.SPACESHIP, 2)
        self.speed = GAME_STATE.difficulty.PLAYER_SPEED
        self.health = GAME_STATE.difficulty.PLAYER_HEALTH
        self.shoot_sound = Sound(AssetsPaths.LASER_SHOOT)
        self.shoot_sound.set_volume(0.5)


    def update(self, dt: float) -> None:
        self.move(dt)

    
    def handle_input(self, event: Event, player_bullets: Group):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.shoot(player_bullets)

    def move(self, dt: float):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.x > 0:
            self.pos_x -= self.speed * dt

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.rect.x + self.rect.width) < SCREEN_WIDTH:
            self.pos_x += self.speed * dt

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.rect.y > 0:
            self.pos_y -= self.speed * dt

        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and (self.rect.y + self.rect.height < SCREEN_HEIGHT):
            self.pos_y += self.speed * dt

        self.rect.x = round(self.pos_x)
        self.rect.y = round(self.pos_y)
        
        # reseta a posicao do player caso ele ultrapasse os limites
        if (self.rect.x < 0):
            self.rect.x = 0
        elif self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.rect.x = (SCREEN_WIDTH - self.rect.width)



    def shoot(self, bullets: Group):
        if (len(bullets) == GAME_STATE.difficulty.MAX_PLAYER_BULLETS):
            return

        if self.health <= 0:
            return
        
        new_bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(new_bullet)
        self.shoot_sound.play()


    
    def receive_damage(self, amount = 100):
        self.health -= amount
        if self.health <= 0:
            self.kill()
