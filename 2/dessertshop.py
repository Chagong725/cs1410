class DessertItem:
    def __init__(self, name=str):
        self.name = name

    def __str__(self):
        return self.name
    

class Candy(DessertItem):
    def __init__(self, name, candy_weight= float, price_per_pound=float):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def __str__(self):
        return self.name
        
    def get_price(self):
        return self.candy_weight * self.price_per_pound 

          
class Cookie(DessertItem):
    def __init__(self, name, cookie_quantity=int, price_per_dozen=float):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def __str__(self):
        return self.name

    def get_price(self):
        return (self.cookie_quantity / 12) * self.price_per_dozen


class IceCream(DessertItem):
    def __init__(self, name, scoop_count=int, price_per_scoop=float):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    
    def __str__(self):
        return self.name
    
    def get_price(self):
        return self.scoop_count * self.price_per_scoop

class Sundae(IceCream):
    def __init__(self,name, scoop_count=int, price_per_scoop=float, topping_name=str, topping_price=float):
        super().__init__(name, scoop_count, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def __str__(self):
        return self.name
      
    def get_price(self):
        return super.get_price() + self.topping_price

class Order:
    def __init__(self):
        self.order = []

    def add(self, item):
        self.order.append(item)
 
    def __len__(self):
        return len(self.order)

def main():
    neworder = Order()
    neworder.add(Candy("Candy Corn", 1.5, .25))
    neworder.add(Candy("Gummy Bears", .25, .35))
    neworder.add(Cookie("Chocolate Chip", 6, 3.99))
    neworder.add(IceCream("Pistachio", 2, .79))
    neworder.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    neworder.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for item in neworder.order:
        print(item)
    print('Total number of items in order:', len(neworder.order))

if __name__ == "__main__":
    main()