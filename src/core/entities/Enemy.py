from pygame.mixer import Sound
from core.constants.constants import AssetsPaths, Settings
from core.entities.Entity import Entity
from core.entities.EnemyBullet import EnemyBullet
from pygame.sprite import Group
from core.state.GameState import GAME_STATE


class Enemy(Entity):

    def __init__(self, x: int, y: int, target_y: int, health: int):
        super().__init__(x=x, y=y, image_path=AssetsPaths.CHICKEN, scale_factor=0.15)
        self.speed = GAME_STATE.difficulty.ENEMY_SPEED
        self.health = health
        self.chicken_death = Sound(AssetsPaths.CHICKEN_DEATH)
        self.target_y = target_y

    def receive_damage(self, amount = 100):
        self.health -= amount
        if self.health <= 0:
            GAME_STATE.increase_score(Settings.SCORE_ENEMY_KILL)
            self.chicken_death.play()
            self.kill()

    def shoot(self, bullets: Group):
        
        new_bullet = EnemyBullet(self.rect.centerx, self.rect.top)
        bullets.add(new_bullet)