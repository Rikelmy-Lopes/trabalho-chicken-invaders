

import pygame
from pygame.mixer import Sound
from pygame.sprite import Group

from constants.constants import PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from core.entities.Bullet import Bullet
from core.entities.Entity import Entity

BLUE_COLOR = (0, 0, 255)



class Player(Entity):
    PLAYER_WIDTH = 100
    PLAYER_HEIGHT = 100

    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, BLUE_COLOR, (self.PLAYER_WIDTH, self.PLAYER_HEIGHT), image_path)
        self.speed = PLAYER_SPEED
        self.health = 100
        self.shoot_sound = Sound('./src/sounds/laser_shoot.wav')
        self.shoot_sound.set_volume(0.5)


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= round(self.speed * dt)

        if keys[pygame.K_RIGHT] and (self.rect.x + self.rect.width) < SCREEN_WIDTH:
            self.rect.x += round(self.speed * dt)

        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= round(self.speed * dt)

        if keys[pygame.K_DOWN] and (self.rect.y + self.rect.height < SCREEN_HEIGHT):
            self.rect.y += round(self.speed * dt)

        # reseta a posicao do player caso ele ultrapasse os limites
        if (self.rect.x < 0):
            self.rect.x = 0
        elif self.rect.x + self.rect.width > SCREEN_WIDTH:
            self.rect.x = (SCREEN_WIDTH - self.rect.width)


    def shoot(self, bullets: Group):
        if (len(bullets) == 0):
            new_bullet = Bullet(self.rect.centerx, self.rect.top)
            bullets.add(new_bullet)
            self.shoot_sound.play()
