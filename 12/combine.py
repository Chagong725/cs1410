from typing import Protocol, runtime_checkable
from abc import abstractmethod

@runtime_checkable
class Combinable(Protocol):

    @abstractmethod
    def can_combine(self, other) -> bool:
        pass
    
    @abstractmethod
    def combine(self, other) -> "Combinable":
        pass
