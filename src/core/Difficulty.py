from enum import Enum

class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3
    VERY_HARD = 4


class DifficultySettings:
    def __init__(
        self,
        difficulty_value: Difficulty,
        enemy_amount: int,
        enemy_health: int,
        enemy_speed: int,
        enemy_bullet_delay: int,
        player_health: int,
        max_player_bullets: int
    ):
        self.difficulty_value = difficulty_value
        self.ENEMY_AMOUNT = enemy_amount
        self.ENEMY_HEALTH = enemy_health
        self.ENEMY_SPEED = enemy_speed
        self.ENEMY_BULLET_DELAY = enemy_bullet_delay
        self.PLAYER_HEALTH = player_health
        self.MAX_PLAYER_BULLETS = max_player_bullets