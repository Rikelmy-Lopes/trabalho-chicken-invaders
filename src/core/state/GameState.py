from constants.constants import DIFFICULTIES
from core.Difficulty import Difficulty



class _GameState:
    """
    Controla os estados do jogo. So pode haver uma única instancia dessa classe (Singleton)
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.score = 0
            cls._instance.difficulty = DIFFICULTIES[Difficulty.NORMAL]

        return cls._instance


    def update_difficulty(self, difficulty: Difficulty):
        self.difficulty = DIFFICULTIES[difficulty]
    
    def increase_score(self, score: int):
        self.score += score


GAME_STATE = _GameState()