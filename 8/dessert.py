from abc import ABC, abstractmethod
from freezer import Freezer, Freeze
from packaging import Packaging

class DessertItem(ABC, Packaging):
    def __init__(self, name=str):
        self.name = name
        self.tax_percent = 7.25
        self.packaging = None
    def __str__(self):
        return self.name
    
    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)

    def __eq__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() == other.calculate_cost()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() < other.calculate_cost()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() > other.calculate_cost()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() <= other.calculate_cost()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() >= other.calculate_cost()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, DessertItem):
            return self.calculate_cost() != other.calculate_cost()
        return NotImplemented

class Candy(DessertItem):
    def __init__(self, name, weight= float, price_per=float):
        super().__init__(name)
        self.weight = weight
        self.price_per = price_per
        self.packaging = "Bag"
    def calculate_cost(self):
        return self.weight * self.price_per
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} ({self.packaging})\n"   \
            f"            {self.weight}lbs         ${self.price_per:.2f}/lbs    ${cost:.2f}   ${tax:.2f}"

class Cookie(DessertItem, Freeze):
    def __init__(self, name, weight=int, price_per=float):
        super().__init__(name)
        self.weight = weight
        self.price_per = price_per
        self.packaging = "Box"
        
    def calculate_cost(self):
        return self.weight / 12 * self.price_per
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.packaging}\n" \
            f"            {self.weight} cookies    ${self.price_per:.2f}/dozen    ${cost:.2f}    ${tax:.2f}"

class IceCream(DessertItem, Freeze):
    def __init__(self, name, weight=int, price_per=float):
        super().__init__(name)
        self.weight = weight
        self.price_per = price_per
        self.packaging = "Bowl"
    
    def calculate_cost(self):
        return self.weight * self.price_per
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.packaging}\n" \
            f"             {self.weight} scoops     ${self.price_per:.2f}/scoop    ${cost:.2f}   ${tax:.2f}"
    
class Sundae(IceCream):
    def __init__(self,name, weight=int, price_per=float, topping_name=str, topping_price=float):
        super().__init__(name, weight, price_per)
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"
        self.item_temperature = "Thawing"
    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.packaging}\n" \
            f"             {self.weight} scoops     ${self.price_per:.2f}/scoop    ${cost:.2f}   ${tax:.2f}"