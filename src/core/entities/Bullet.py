from constants.constants import BULLET_SPEED
from core.entities.Entity import Entity

WHITE_COLOR = (255, 255, 255)

class Bullet(Entity):
        
    def __init__(self, x: int, y: int):
        super().__init__(x, y, WHITE_COLOR, (5, 10), './src/images/laserBullet.png', 0.4)
        self.speed = BULLET_SPEED


    def update(self, dt: float) -> None:
        self.pos_y -= self.speed * dt
        self.rect.y = round(self.pos_y)
        
        if self.rect.y < 0:
            self.kill()