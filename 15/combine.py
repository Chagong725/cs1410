from typing import Protocol
import typing


class Combinable(Protocol):
    @typing.runtime_checkable
    def can_combine(self, other: "Combinable") -> bool:
        pass

    def combine(self, other: "Combinable") -> "Combinable":
        pass
