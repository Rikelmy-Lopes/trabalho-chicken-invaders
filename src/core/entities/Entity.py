
from typing import Tuple

import pygame
from pygame import Surface
from pygame.sprite import Sprite


class Entity(Sprite):

    def __init__(
            self, 
            x: int, 
            y: int, 
            image_path: str | None = None, 
            scale_factor: float = 1, 
            color: Tuple[int, int, int] = (255, 0, 0)
        ):
        super().__init__()
        base_size = (50, 50)
        
        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()
            rect = self.image.get_rect()
            new_size = (int(rect.width * scale_factor), int(rect.height * scale_factor))
            self.image = pygame.transform.smoothscale(self.image, new_size)
        else:
            scaled_size = (int(base_size[0] * scale_factor), int(base_size[1] * scale_factor))
            self.image = Surface(scaled_size)
            self.image.fill(color)
            
        self.rect = self.image.get_rect(topleft=(x, y))
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        self.speed = None