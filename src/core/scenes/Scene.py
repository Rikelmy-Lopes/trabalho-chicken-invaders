from abc import ABC, abstractmethod
from pygame.event import Event

from core.State import State

class Scene(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def update(self, events: list[Event]) -> State:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass