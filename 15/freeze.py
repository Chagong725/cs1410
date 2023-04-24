from typing import Protocol
from dessert import DessertItem


class Freeze(Protocol):
    def chill(self) -> None:
        pass

    def thaw(self) -> None:
        pass

    def temperature(self) -> str:
        pass


class Freezer:
    def __init__(self):
        self.items = []

    def put(self, item: DessertItem) -> None:
        item.chill()
        self.items.append(item)

    def take(self, item_name: str) -> str:
        for i, item in enumerate(self.items):
            if type(item).__name__.lower() == item_name.lower():
                self.items.pop(i)
                item.thaw()
                return item_name
            else:
                return item_name