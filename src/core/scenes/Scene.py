from abc import ABC, abstractmethod
from pygame.event import Event

class Scene(ABC):

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def update(self, events: list[Event]):
        pass

    @abstractmethod
    def reset(self) -> None:
        pass