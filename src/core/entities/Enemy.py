


import pygame

from core.entities.Entity import Entity

RED_COLOR = (255, 0, 0)


class Enemy(Entity):

    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, RED_COLOR, (100, 100), image_path)
        self.health = 100
        self.chicken_death = pygame.mixer.Sound('./src/sounds/chicken_death.mp3')

    def receive_damage(self, amount = 100):
        self.health -= amount
        if self.health <= 0:
            self.chicken_death.play()
            self.kill()