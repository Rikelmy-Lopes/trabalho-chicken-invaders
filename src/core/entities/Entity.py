
from typing import Tuple

import pygame
from pygame import Surface
from pygame.sprite import Sprite


class Entity(Sprite):

    def __init__(self, x: int, y: int, color: Tuple[int, int, int], size: Tuple[int, int], image_path=None, scale_factor: float = 1):
        super().__init__()
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            rect = self.image.get_rect()
            new_size = (int(rect.width * scale_factor), int(rect.height * scale_factor))
            self.image = pygame.transform.smoothscale(self.image, new_size)
        else:
            self.image = Surface(size)
            self.image.fill(color)
            
        self.rect = self.image.get_rect(topleft=(x, y)) 
        self.speed = None