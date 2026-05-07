
# informações tecnicas do jogo
from core.Difficulty import Difficulty, DifficultySettings


FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BULLET_SPEED = 500
DT_DIVISOR = 1000.0
SELECTED_COLOR_MENU = (30, 144, 255)
UNSELECTED_COLOR_MENU = (176, 196, 222)
FONT_PATH = "./src/fonts/PressStart2P-Regular.ttf"
FONT_SIZE_BIG = 32
FONT_SIZE_MEDIUM = 24
FONT_SIZE_SMALL = 9



DIFFICULTIES = {
    Difficulty.EASY: DifficultySettings(
        Difficulty.EASY,
        enemy_amount=6,
        enemy_health=100,
        enemy_speed=50,
        enemy_bullet_delay=1000,
        enemy_bullet_speed=150,
        player_speed=200,
        player_health=300,
        max_player_bullets=2
    ),
    Difficulty.NORMAL: DifficultySettings(
        Difficulty.NORMAL,
        enemy_amount=6,
        enemy_health=200,
        enemy_speed=50,
        enemy_bullet_delay=1000,
        enemy_bullet_speed=150,
        player_speed=200,
        player_health=200,
        max_player_bullets=1
    ),
    Difficulty.HARD: DifficultySettings(
        Difficulty.HARD,
        enemy_amount=12,
        enemy_health=200,
        enemy_speed=75,
        enemy_bullet_delay=1000,
        enemy_bullet_speed=400,
        player_speed=100,
        player_health=100,
        max_player_bullets=1
    ),
    Difficulty.VERY_HARD: DifficultySettings(
        Difficulty.VERY_HARD,
        enemy_amount=12,
        enemy_health=300,
        enemy_speed=75,
        enemy_bullet_delay=800,
        enemy_bullet_speed=400,
        player_speed=100,
        player_health=100,
        max_player_bullets=1
    )
}