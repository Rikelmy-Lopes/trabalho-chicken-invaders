
from constants.constants import BULLET_SPEED
from entities.Entity import Entity

WHITE_COLOR = (255, 255, 255)

class Bullet(Entity):
        
    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, WHITE_COLOR, (5, 10), image_path)
        self.speed = BULLET_SPEED


    def update(self, dt: float) -> None:
        self.rect.y -= round(self.speed * dt)
        
        if self.rect.y < 0:
            self.kill()


    