from abc import ABC, abstractmethod
from payment import PayType, Payment
# from combine import Combinable


class DessertItem(ABC):
    """Superclass of the Dessert Project"""
    def __init__(self, name="", unit=float, price=float, tax_percent=7.25):
        self.tax_percent = tax_percent
        self.name = name
        self.price = price
        self.unit = unit
        self.packaging = None

    @abstractmethod
    def calculate_cost(self):
        total_price = self.price
        return float(total_price)

    def calculate_tax(self):
        tax_rate = self.tax_percent / 100
        total_cost = float(self.calculate_cost()) * tax_rate
        return total_cost

    def chill(self):
        pass

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price <= other.price

    def __le__(self, other):
        return self.price >= other.price


class Candy(DessertItem):
    """Candy class defines the weight of the candy and the price per pound"""
    def __init__(self, name="", unit=float, price=float):
        super().__init__(name, unit, price)
        self.packaging = "Bag"

    def calculate_cost(self):
        cost = float(self.price) * float(self.unit)
        return cost

    def __str__(self):
        return {f"{self.name}, ({self.packaging}), {self.unit}lbs, ${self.price()}/lb, ${self.calculate_cost()}, "
                f"${self.calculate_tax()}"}

    def can_combine(self, other: "Candy") -> bool:
        if isinstance(other, Candy):
            return self.name == other.name and self.__eq__(other)
        return False

    def combine(self, other: "Candy") -> "Candy":
        if self.can_combine(other):
            self.unit = float(self.unit) + float(other.unit)
            # self.unit += other.unit
            return self


class Cookie(DessertItem):
    """Cookie class defines the amount of cookies and the price per dozen"""
    def __init__(self, name="", unit=float, price=float):
        super().__init__((name + " Cookies"), unit, price)
        self.packaging = "Box"
        self.freezer = "Chilled"

    def calculate_cost(self):
        cost = ((float(self.price) / 12) * float(self.unit))
        return cost

    def __str__(self):
        return {f"{self.name}, ({self.packaging}), {self.unit}/cookies, {self.price()}/dozen, ${self.calculate_cost()},"
                f"${self.calculate_tax()}"}

    def can_combine(self, other: "Cookie") -> bool:
        if isinstance(other, Cookie):
            return self.name == other.name and self.__eq__(other)
        return False

    def combine(self, other: "Cookie") -> "Cookie":
        if self.can_combine(other):
            self.unit = float(self.unit) + float(other.unit)
            # self.unit += other.unit
            return self


class IceCream(DessertItem):
    """Ice Cream class defines the scoop count and the price per"""
    def __init__(self, name="", unit=float, price=float):
        super().__init__((name + " Ice Cream"), unit, price)
        self.packaging = "Bowl"

    def calculate_cost(self):
        cost = float(self.price) * float(self.unit)
        return cost

    def __str__(self):
        return {f"{self.name}, ({self.packaging}), {self.unit}/scoops, {self.price}/scoop, ${self.calculate_cost()}, "
                f"${self.calculate_tax()}"}


class Sundae(IceCream, DessertItem):
    """Sundae class defines the toppings and price per"""
    def __init__(self, name="", unit=int, price=float, topping_name="", topping_price=float):
        super().__init__(name, unit, price)
        self.name = topping_name + " " + name + " Sundae"
        self.topping_name = topping_name
        self.topping_price = topping_price
        self.packaging = "Boat"

    def calculate_cost(self):
        cost = (float(self.price) * float(self.unit)) + float(self.topping_price)
        return cost

    def __str__(self):
        return {f" {self.name}, ({self.packaging}), {self.unit}/scoops, {self.price}/scoop, ${self.calculate_cost()}, "
                f"${self.calculate_tax()} \n{self.topping_name}, 1, ${self.topping_price}"}


class Order(Payment):
    def __init__(self, pay_type: PayType):
        super().__init__(pay_type)
        self.order = []
        self.pay_method = Payment(PayType.CASH)

    def get_dessert_order(self):
        return self.order

    def add(self, item):
        if (not isinstance(item, Candy) and not isinstance(item, Cookie)) or not any(item.can_combine(other) for other in self.order):
            self.order.append(item)
        elif isinstance(item, Candy) or isinstance(item, Cookie):
            for i, other in enumerate(self.order):
                if item.can_combine(other):
                    self.order[i] = item.combine(other)
                    break

    def order_cost(self):
        cost = 0
        for item in self.order:
            cost += item.calculate_cost()
        return cost

    def order_tax(self):
        tax = 0
        for item in self.order:
            tax += item.calculate_tax()
        return tax

    def item_count(self):
        return len(self.order)

    def set_pay_method(self, value):
        self.pay_method = Payment(PayType(value))
        return self.pay_method

    def get_payment_method(self):
        return self.pay_method.__str__()

    def __str__(self):
        order_str = ""
        for item in self.order:
            order_str += f"{self.add(item)}, {round(item.calculate_cost(), 2)}, {round(item.calculate_tax(), 2)}, {self.pay_method}\n"
        return order_str

    def __len__(self):
        return len(self.order)