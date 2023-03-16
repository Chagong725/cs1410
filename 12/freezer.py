from typing import Protocol
class Freezer:
    def __init__(self):
        self.my_freezer = []
    def add_2_freezer(self, item):
        self.my_freezer.append(item)

class Freeze(Protocol):
    _temperature: str = "thawing"

    def chill(self):
        self._temperature = "chilling"

    def thaw(self) -> str:
        self._temperature = "thawing"
        return self._temperature

    def get_temperature(self) -> str:
        return getattr(self, '_temperature', 'thawing')