from abc import ABC, abstractmethod
from receipt import *
class DessertItem(ABC):
    def __init__(self, name=str):
        self.name = name
        self.tax_percent = 7.25
    def __str__(self):
        return self.name
    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return (self.calculate_cost() * (self.tax_percent / 100))

class Candy(DessertItem):
    def __init__(self, name, candy_weight= float, price_per_pound=float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound
class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity=int, price_per_dozen=float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    def calculate_cost(self):
        return self.cookie_quantity / 12 * self.price_per_dozen
class IceCream(DessertItem):
    def __init__(self, name, scoop_count=int, price_per_scoop=float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    def calculate_cost(self):
        return self.scoop_count * self.price_per_scoop
    
class Sundae(IceCream):
    def __init__(self,name, scoop_count=int, price_per_scoop=float, topping_name=str, topping_price=float):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price
    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price
class Order:
    def __init__(self):
        self.order = []
    def add_item(self, item):
        self.order.append(item)
 
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        total_cost = 0
        for items in self.order:
            total_cost += items.calculate_cost()
        return total_cost
    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()
        return total_tax
def main():
    my_order = Order()

    my_order.add_item(Candy("Candy Corn", 1.5, 0.25))
    my_order.add_item(Candy("Gummy Bears", 0.25, 0.35))
    my_order.add_item(Cookie("Chocolate Chip", 6, 3.99))
    my_order.add_item(IceCream("Pistachio Cookie", 2, 0.79))
    my_order.add_item(Sundae("Vanilla", 3, 0.69, "Hot Fudge", 1.29))
    my_order.add_item(Cookie("Oatmeal Raisin", 2, 3.45))

    cost = my_order.order_cost()
    tax = my_order.order_tax()
    total_cost = cost + tax
    total = my_order.__len__()
    make_receipt(my_order.order, "receipt.pdf", cost, total_cost, tax, total)
if __name__ == "__main__":
    main()