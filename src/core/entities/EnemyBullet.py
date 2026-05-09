from core.constants.constants import AssetsPaths, Settings
from core.entities.Entity import Entity
from core.state.GameState import GAME_STATE

class EnemyBullet(Entity):
        
    def __init__(self, x: int, y: int):
        super().__init__(x=x, y=y, image_path=AssetsPaths.EGG, scale_factor=0.5)
        self.speed = GAME_STATE.difficulty.ENEMY_BULLET_SPEED


    def update(self, dt: float) -> None:
        self.pos_y += self.speed * dt
        self.rect.y = round(self.pos_y)
        
        if self.rect.y > Settings.SCREEN_HEIGHT:
            self.kill()