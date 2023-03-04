from receipt import *
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae
from freezer import Freezer, Freeze
from payment import Payment

customer_db: dict[str, object] = {}

class Order:
    def __init__(self):
      self.order = []
    def add_item(self, item):
        for orderitems in self.order:
            if orderitems.can_combine(item):
                item = item.combine(orderitems)
                self.order.remove(orderitems)
            else: pass

        self.order.append(item)
 
    def __len__(self):
        return len(self.order)
    def order_cost(self):
        total_cost = 0
        for items in self.order:
            total_cost += items.calculate_cost()
        return round(total_cost, 2)
    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()
        return round(total_tax, 2)

    def print_order(self, Customer):
        payment = self.choose_payment()
        self.orderitems()
        print("-----------------------RECEIPT-----------------------")
        print("_____________________________________________________")
        print("Name        Quantity      Price         Cost     Tax")
        print("_____________________________________________________")    
        for item in self.order:
            print(item)
            print('')
        print("_____________________________________________________")
        print("Total number of items in order: ", len(self.order))
        print(f"Subtotal: ${self.order_cost():.2f}, Tax: ${self.order_tax():.2f}")
        print(f"Total: ${self.order_cost() + self.order_tax():.2f}")
        print("_____________________________________________________")
        print("Pay for with", payment)
        print("_____________________________________________________")
        print("Customer name: ", Customer.name, "Customer ID: ", Customer.customerid, "Total Orders: ", len(Customer.order_history))

    def choose_payment(self):
        while True:
            for payment_method in Payment:
                print(f"{payment_method.value}. {payment_method.name}")
            try:
                print("What form of payment will be used? (CASH, CARD, PHONE):")
                payment_choice = int(input())
                return Payment(payment_choice).payment_method()
                break
            
            except ValueError:
                print("Please enter a number between 1 and 3.")

    def orderitems(self):
        self.order.sort()

class Customer:
    # Class that represents a customer of the dessert shop
    def __init__(self, name = str):
        self.name: str = name
        self.order_history: list[Order] = []
        self.customerid: int = 0
        number_of_orders = len(self.order_history)

    def add2history(self, order):
        #add the order to history
        self.order_history.append(order)
        return self

    def figure_customerid(self, customer_db):
        #figure out the customer id
        self.customerid = len(customer_db)
        return self
    
def stock_freezer():
    freezer = Freezer()
    for i in range(10):
        freezer.add_2_freezer(IceCream('Vanilla', 3, .5))
        freezer.add_2_freezer(IceCream('Chocolate', 3, .5))
        freezer.add_2_freezer(IceCream('Mint Chocolate', 3, .5))
        freezer.add_2_freezer(Cookie('Chocolate Chip', 3, 5.5))
        freezer.add_2_freezer(Cookie('Potato Chip', 3, 5.5))
        freezer.add_2_freezer(Cookie('Pretzel', 3, 5.5))
        freezer.add_2_freezer(Sundae('Vanilla', 3, .5, 'Sprinkles'))
        freezer.add_2_freezer(Sundae('Chocolate', 3, .5, 'Caramel'))
        freezer.add_2_freezer(Sundae('Mint Chocolate', 3, .5, 'Oatmeal Raisin'))

    for i in freezer.my_freezer:
        i.chill()
    return freezer

def main_menu(my_order: Order, freezer) -> None:
    continue_order = True
    while continue_order == True:
        print('1: Candy')
        print('2: Cookies')
        print('3: IceCream')
        print('4: Sundae')
        choice = input('What would you like to add to the order? (1-4, Enter for done): ')

        if choice == '1':
            user_prompt_candy(my_order)
        elif choice == '2':
            user_prompt_cookie(my_order, freezer)
        elif choice == '3':
            user_prompt_icecream(my_order, freezer)
        elif choice == '4':
            user_prompt_sundae(my_order, freezer)
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
        price = 2.25
    elif candy == '2':
        candy = 'Gummy Bears'
        price = .5
    elif candy == '3':
        candy = "Candy Corn"
        price = 2.0
    elif candy == "":
        print('Returning to main menu')
        main_menu()
    else:
        print('Invalid Input: please use the prompts provided')
        user_prompt_candy(my_order)
    weight = input('How many lbs of candy would you like? ')
    weight = float(weight)
    print(f'Adding {weight} lbs of {candy} to your order.'.format(weight, candy))
    candy_item = Candy(candy,weight, price )
    my_order.add_item(candy_item)

def user_prompt_cookie(my_order, freezer):
    print('1. Chocolate Chip ($3.00 per dozen) 2. Potato Chip ($3.5 per dozen) 3. Pretzel ($2.00 per dozen)')
    cookie = input('Which cookie would you like to order? ')
    if cookie == '1':
        cookie = "Chocolate Chip Cookie"
        price = 3.0
    elif cookie == '2':
        cookie = "Potato Chip"
        price = 3.25
    elif cookie == '3':
        cookie = "Pretzel"
        price = 2.0
    elif cookie == "":
        user_prompt_cookie(my_order)
    else:
        print("Invalid syntax:  Please use the options provided")
        user_prompt_cookie(my_order)
    amount = input('How many cookies would you like? ')
    amount = int(amount)
    cookie_item = Cookie(cookie, amount, price)

    cookie_found = False
    for item in freezer.my_freezer:
        if item.name == cookie_item.name:
            item.thaw()
            freezer.my_freezer.remove(item)
            my_order.add_item(item)
            cookie_found = True
            break
    if not cookie_found:
        my_order.add_item(cookie_item)

def user_prompt_icecream(my_order, freezer):
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
    icecream_item = IceCream(icecream, scoops, price)
    icecream_found = False
    for item in freezer.my_freezer:
        if item.name == icecream_item.name:
            item.thaw()
            freezer.my_freezer.remove(item)
            my_order.add_item(item)
            icecream_found = True
            break
    
    if not icecream_found:
        my_order.add_item(icecream_item)
    print(f'Adding a {icecream} flavored Ice Cream with {scoops} scoops'.format(icecream, scoops))
    
def user_prompt_sundae(my_order, freezer):
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
    sundae_item = Sundae(icecream, scoops, price, topping, topprice)

    sundae_found = False
    for item in freezer.my_freezer:
        if item.name == sundae_item.name and item.topping == sundae_item.topping:
            item.thaw()
            freezer.my_freezer.remove(item)
            my_order.add_item(item)
            sundae_found = True
            break
    
    if not sundae_found:
        my_order.add_item(sundae_item)
        
def main():
    continueorder = True
    while continueorder:
        freezer = stock_freezer()

        my_order = Order()

        try:
            main_menu(my_order, freezer)
        except:
            main_menu(my_order, freezer)

        customername = input("Enter the customer name: ")
        new_customer = Customer(customername)
        if new_customer.name not in customer_db:
            customer_db[new_customer.name] = new_customer
            new_customer.figure_customerid(customer_db)
        else:
            new_customer = customer_db[new_customer.name]
        new_customer.add2history(my_order.order)

        my_order.print_order(new_customer)
        
        # cost = round(my_order.order_cost(), 2)
        # tax = round(my_order.order_tax(), 2)
        # total_cost = round(cost + tax, 2)
        # pay = my_order.choose_payment().upper()
        # total = my_order.__len__()

        # make_receipt(my_order.order, "receipt.pdf", cost, total_cost,tax, total, pay)
        anotherorder = input('Anything else? (y/n)')
        if anotherorder == 'Y' or anotherorder == 'y':
            continueorder = True
            my_order.order = []

        else:
            continueorder = False 

if __name__ == "__main__":
    main()