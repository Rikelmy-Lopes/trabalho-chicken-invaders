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
        enemy_fire_rate: int,
        enemy_bullet_speed: int,
        player_speed: int,
        player_health: int,
        player_bullet_speed: int,
        player_fire_rate: int
    ):
        self.difficulty_value = difficulty_value
        self.ENEMY_AMOUNT = enemy_amount
        self.ENEMY_HEALTH = enemy_health
        self.ENEMY_SPEED = enemy_speed
        self.ENEMY_FIRE_RATE = enemy_fire_rate
        self.ENEMY_BULLET_SPEED = enemy_bullet_speed
        self.PLAYER_SPEED = player_speed
        self.PLAYER_HEALTH = player_health
        self.PLAYER_BULLET_SPEED = player_bullet_speed
        self.PLAYER_FIRE_RATE = player_fire_rate