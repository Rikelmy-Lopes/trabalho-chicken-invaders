

import pygame

from constants.constants import PLAYER_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH
from entities.Bullet import Bullet
from entities.Entity import Entity

BLUE_COLOR = (0, 0, 255)

class Player(Entity):

    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, BLUE_COLOR, (100, 100), image_path)
        self.speed = PLAYER_SPEED
        self.health = 100


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


    def shoot(self, bullets: pygame.sprite.Group):
        new_bullet = Bullet(self.rect.centerx, self.rect.top)
        bullets.add(new_bullet)
