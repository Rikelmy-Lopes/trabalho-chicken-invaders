from core.constants.constants import AssetsPaths
from core.entities.Entity import Entity
from core.state.GameState import GAME_STATE

class PlayerBullet(Entity):
        
    def __init__(self, x: int, y: int):
        super().__init__(x=x, y=y, image_path=AssetsPaths.LASER_BULLET, scale_factor=0.4)
        self.speed = GAME_STATE.difficulty.PLAYER_BULLET_SPEED


    def update(self, dt: float) -> None:
        self.pos_y -= self.speed * dt
        self.rect.y = round(self.pos_y)
        
        if self.rect.y < 0:
            self.kill()