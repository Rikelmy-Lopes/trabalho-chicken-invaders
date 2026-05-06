


from pygame.mixer import Sound

from core.entities.Entity import Entity
from core.entities.EnemyBullet import EnemyBullet
from pygame.sprite import Group

from core.state.GameState import GAME_STATE

RED_COLOR = (255, 0, 0)


class Enemy(Entity):

    def __init__(self, x: int, y: int, max_y: int, health: int, image_path=None):
        super().__init__(x, y, RED_COLOR, (50, 50), image_path)
        self.speed = GAME_STATE.difficulty.ENEMY_SPEED
        self.health = health
        self.chicken_death = Sound('./src/sounds/chicken_death.mp3')
        self.max_y = max_y

    def receive_damage(self, amount = 100):
        self.health -= amount
        if self.health <= 0:
            self.chicken_death.play()
            self.kill()

    def shoot(self, bullets: Group):
        
        new_bullet = EnemyBullet(self.rect.centerx, self.rect.top)
        bullets.add(new_bullet)
        # self.shoot_sound.play()