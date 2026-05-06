from constants.constants import SCREEN_HEIGHT
from core.entities.Entity import Entity
from core.state.GameState import GAME_STATE

WHITE_COLOR = (255, 255, 255)

class EnemyBullet(Entity):
        
    def __init__(self, x, y):
        super().__init__(x, y, WHITE_COLOR, (5, 10), './src/images/laserBullet.png', 0.4)
        self.speed = GAME_STATE.difficulty.ENEMY_BULLET_SPEED


    def update(self, dt: float) -> None:
        self.rect.y += round(self.speed * dt)
        
        if self.rect.y > SCREEN_HEIGHT:
            self.kill()