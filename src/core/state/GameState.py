from core.constants.constants import Difficulties
from core.Difficulty import Difficulty
from core.SceneEnum import SceneEnum



class _GameState:
    """
    Controla os estados do jogo. So pode haver uma única instancia dessa classe (Singleton)
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.score = 0
            cls._instance.difficulty = Difficulties.NORMAL
            cls._instance.current_scene = SceneEnum.MENU

        return cls._instance


    def update_difficulty(self, difficulty: Difficulty):
        self.difficulty = Difficulties.get(difficulty)
    
    def increase_score(self, score: int):
        self.score += score

    def set_current_scene(self, scene: SceneEnum):
        self.current_scene = scene

    def reset(self):
        self.score = 0


GAME_STATE = _GameState()