
from typing import Tuple

import pygame


class Entity(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, color: Tuple[int, int, int], size: Tuple[int, int], image_path=None):
        super().__init__()
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
        else:
            self.image = pygame.Surface(size)
            self.image.fill(color)
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = None