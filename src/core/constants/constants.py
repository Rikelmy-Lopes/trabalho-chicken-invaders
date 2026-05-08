
# informações tecnicas do jogo
from core.Difficulty import Difficulty, DifficultySettings
from core.utils.utils import resolve_path

class Settings:
    FPS = 60
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    DT_DIVISOR = 1000.0
    SELECTED_COLOR_MENU = (30, 144, 255)
    UNSELECTED_COLOR_MENU = (176, 196, 222)
    FONT_SIZE_BIG = 32
    FONT_SIZE_MEDIUM = 24
    FONT_SIZE_SMALL = 9


class AssetsPaths:
    FONT = resolve_path("assets/fonts/PressStart2P-Regular.ttf")
    SPACE_HEROES = resolve_path('assets/musics/space_heroes.ogg')
    MENU_HIGHLIGHT = resolve_path('assets/sounds/menu_highlight.ogg')
    MENU_SELECTION = resolve_path('assets/sounds/menu_selection.wav')
    LASER_SHOOT = resolve_path('assets/sounds/laser_shoot.wav')
    CHICKEN_DEATH = resolve_path('assets/sounds/chicken_death.mp3')
    SPACE = resolve_path('assets/images/space.png')
    LASER_BULLET = resolve_path('assets/images/laserBullet.png')
    SPACESHIP = resolve_path('assets/images/spaceship.png')
    CHICKEN = resolve_path('assets/images/chicken.png')
    EGG = resolve_path('assets/images/egg.png')


class Difficulties:
    EASY = DifficultySettings(
        difficulty_value=Difficulty.EASY,
        enemy_amount=6,
        enemy_health=100,
        enemy_speed=50,
        enemy_bullet_delay=1000,
        enemy_bullet_speed=150,
        player_speed=200,
        player_health=300,
        player_max_bullets=2,
        player_bullet_speed=500
    )

    NORMAL = DifficultySettings(
        difficulty_value=Difficulty.NORMAL,
        enemy_amount=6,
        enemy_health=200,
        enemy_speed=50,
        enemy_bullet_delay=1000,
        enemy_bullet_speed=150,
        player_speed=200,
        player_health=200,
        player_max_bullets=1,
        player_bullet_speed=500
    )

    HARD = DifficultySettings(
        difficulty_value=Difficulty.HARD,
        enemy_amount=12,
        enemy_health=200,
        enemy_speed=75,
        enemy_bullet_delay=1000,
        enemy_bullet_speed=400,
        player_speed=100,
        player_health=100,
        player_max_bullets=1,
        player_bullet_speed=500
    )

    VERY_HARD = DifficultySettings(
        difficulty_value=Difficulty.VERY_HARD,
        enemy_amount=12,
        enemy_health=300,
        enemy_speed=75,
        enemy_bullet_delay=800,
        enemy_bullet_speed=400,
        player_speed=100,
        player_health=100,
        player_max_bullets=1,
        player_bullet_speed=500
    )

    @staticmethod
    def get(difficulty: Difficulty) -> DifficultySettings:
        if difficulty == Difficulty.EASY:
            return Difficulties.EASY
        elif difficulty == Difficulty.NORMAL:
            return Difficulties.NORMAL
        elif difficulty == Difficulty.HARD:
            return Difficulties.HARD
        else:
            return Difficulties.VERY_HARD

