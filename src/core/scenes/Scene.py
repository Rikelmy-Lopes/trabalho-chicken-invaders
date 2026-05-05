from abc import ABC, abstractmethod
from pygame.event import Event

from core.SceneEnum import SceneEnum

class Scene(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def update(self, events: list[Event]) -> SceneEnum:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass