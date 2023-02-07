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

def main_menu(my_order):
    continue_order = True
    while continue_order == True:
        print('1: Candy')
        print('2: Cookies')
        print('3: IceCream')
        print('4: Sundae')
        print('5: Total Order So Far')
        print('Type the number of the option you would like to choose: ')
        choice = input('What would you like to add to the order? (1-4, Enter for done): ')

        if choice == '1':
            user_prompt_candy(my_order)
        elif choice == '2':
            user_prompt_cookie(my_order)
        elif choice == '3':
            user_prompt_icecream(my_order)
        elif choice == '4':
            user_prompt_sundae(my_order)
        elif choice == '':
            continue_order = False
        elif choice == '5':
            print(my_order)
        else:
            print("Invalid input, please use the provided interface.")


def user_prompt_candy(my_order):
    print('1: ChupaChups ($1.25 per lbs) 2: Gummy Bears (.50 per lbs) 3: Candy Corn ($2.00 per lbs)')
    candy = input("Enter type of candy :")
    if candy == '1':
        candy = 'ChupaChups'
        price = 1.25
    elif candy == '2':
        candy = 'Gummy Bears'
        price = .5
    elif candy == '3':
        candy == "Candy Corn"
        price = 2.0
    elif candy == "":
        print('Returning to main menu')
        main_menu()
    else:
        print('Invalid Input: please use the prompts provided')
        user_prompt_candy(my_order)

    weight = input('Enter the lbs of candy: ')
    weight = float(weight)
    print(f'Adding {weight} lbs of {candy} to your order.'.format(weight, candy))

    my_order.append(('Candy', candy, weight, price))



def user_prompt_cookie(my_order):
    print('1. Chocolate Chip ($3.00 per dozen) 2. Potato Chip ($3.5 per dozen) 3. Pretzel ($2.00 per dozen)')
    cookie = input('Enter the type of cookie: ')

    if cookie == '1':
        cookie = "Chocolate Chip Cookie"
        price = 3.0
    elif cookie == '2':
        cookie = "Potato Chip"
        price = 3.5
    elif cookie == '3':
        cookie = "Pretzel"
        price = 2.0
    elif cookie == "":
        user_prompt_cookie(my_order)
    else:
        print("Invalid syntax:  Please use the options provided")
        user_prompt_cookie(my_order)

    amount = input('Enter the quantity purchased: ')
    amount = int(amount)

    my_order.append(('Cookie', cookie, amount, price))

def user_prompt_icecream(my_order):
    print('1. Vanilla ($2.25 per scoop) 2. Chocolate ($2.25 per scoop) 3. Mint Chocolate Chip ($4.50 per scoop)')
    icecream = input('Enter the type of ice cream: ')
    if icecream == '1':
        icecream = 'Vanilla Ice Cream'
        price = 2.25
    elif icecream == '2':
        icecream = 'Chocolate Ice Cream'
        price = 2.25
    elif icecream == '3':
        icecream = 'Mint Chocolate Chip Ice Cream'
        price = 4.5
    elif icecream == '':
        main_menu(my_order)
    else:
        print('Improper syntax: please use the provided menu')
        print(type(icecream))
        user_prompt_icecream(my_order)

    scoops = input('Enter the number of scoops: ')
    scoops = int(scoops)

    my_order.append(('Ice Cream', icecream, scoops, price))
    print(f'Adding a {icecream} flavored Ice Cream with {scoops} scoops'.format(icecream, scoops))
    
def user_prompt_sundae(my_order):
    print('1. Vanilla ($2.25 per scoop) 2. Chocolate ($2.25 per scoop) 3. Mint Chocolate Chip ($4.50 per scoop)')
    icecream = input('Enter the type of ice cream: ')
    if icecream == '1':
        icecream = 'Vanilla Ice Cream'
        price = 2.25
    elif icecream == '2':
        icecream = 'Chocolate Ice Cream'
        price = 2.25
    elif icecream == '3':
        icecream = 'Mint Chocolate Chip Ice Cream'
        price = 4.5
    elif icecream == '':
        main_menu(my_order)
    else:
        print('Improper syntax: please use the provided menu')
        user_prompt_sundae(my_order)

    scoops = input('Enter the number of scoops: ')
    scoops = int(scoops)

    
    print('1. Sprinkles (.25 cents) 2. Caramel (.50 cents) 3. Oatmeal Raisin (.30 cents)')
    topping = input('Enter the topping: ')
    
    if topping == '1':
        topping = 'Sprinkles'
        topprice = .25
    elif topping == '2':
        topping == "Caramel"
        topprice = .50
    elif topping == '3':
        topping = 'Oatmeal Raisin'
        topprice = .30
    elif topping == '':
        main_menu()
    else:
        print('Invalid input: Please use the menu options')

    print(f'Adding a {icecream} flavored sundae with {topping} on top'.format(icecream, topping))

    my_order.append(('Sundae', icecream, scoops, price, topping, topprice))
    
    


def main():
    my_order = []
    main_menu(my_order)

    new_order = Order()
    for item in my_order:
        if item[0] == 'Candy':
            new_order.add_item(Candy(item[1], item[2], item[3]))
        elif item[0] == 'Cookie':
            new_order.add_item(Cookie(item[1], item[2], item[3]))
        elif item[0] == 'Ice Cream':
            print(item)
            new_order.add_item(IceCream(item[1], item[2], item[3]))
            
        elif item[0] == 'Sundae':
            new_order.add_item(Sundae(item[1], item[2], item[3], item[4], item[5]))


    # Calculate the cost and tax of the order
    cost = new_order.order_cost()
    tax = new_order.order_tax()
    total_cost = cost + tax
    total = new_order.__len__()
    make_receipt(new_order.order, "receipt.pdf", cost, total_cost, tax, total)



if __name__ == "__main__":
    main()