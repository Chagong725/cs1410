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

class Candy(DessertItem):
    def __init__(self, name, candy_weight= float, price_per_pound=float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
        self.packaging = "Bag"
    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} ({self.packaging})\n"   \
            f"            {self.candy_weight}lbs         ${self.price_per_pound:.2f}/lbs    ${cost:.2f}   ${tax:.2f}"

class Cookie(DessertItem, Freeze):
    def __init__(self, name, cookie_quantity=int, price_per_dozen=float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
        self.packaging = "Box"
        
    def calculate_cost(self):
        return self.cookie_quantity / 12 * self.price_per_dozen
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.packaging}\n" \
            f"            {self.cookie_quantity} cookies    ${self.price_per_dozen:.2f}/dozen    ${cost:.2f}    ${tax:.2f}"

class IceCream(DessertItem, Freeze):
    def __init__(self, name, scoop_count=int, price_per_scoop=float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
        self.packaging = "Bowl"
    
    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop
    
    def __str__(self):
        cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} {self.packaging}\n" \
            f"             {self.scoop_count} scoops     ${self.price_per_scoop:.2f}/scoop    ${cost:.2f}   ${tax:.2f}"
    
class Sundae(IceCream):
    def __init__(self,name, scoop_count=int, price_per_scoop=float, topping_name=str, topping_price=float):
        super().__init__(name, scoop_count, price_per_scoop)
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
            f"             {self.scoop_count} scoops     ${self.price_per_scoop:.2f}/scoop    ${cost:.2f}   ${tax:.2f}"