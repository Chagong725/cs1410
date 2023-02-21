from receipt import *
from dessert import DessertItem, Candy, Cookie, IceCream, Sundae


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
        return round(total_cost, 2)

    def order_tax(self):
        total_tax = 0
        for item in self.order:
            total_tax += item.calculate_tax()

        return round(total_tax, 2)

    def print_order(self):
        print("-----------------------RECEIPT-----------------------")

        for item in self.order:
            print(item)
            print('')

def main_menu(my_order: Order) -> None:
    continue_order = True
    while continue_order == True:
        print('1: Candy')
        print('2: Cookies')
        print('3: IceCream')
        print('4: Sundae')
        # print('5: Total Order So Far')
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
    
    candy_item = Candy(candy,weight, price )
    my_order.add_item(candy_item)



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
    
    cookie_item = Cookie(cookie, amount, price)
    my_order.add_item(cookie_item)

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
    icecream_item = IceCream(icecream, scoops, price)
    
    my_order.add_item(icecream_item)
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
    sundae_item = Sundae(icecream, scoops, price, topping, topprice)
    my_order.add_item(sundae_item)
    
    


def main():
   
    my_order = Order()

    try:
        main_menu(my_order)
    except:
        main_menu(my_order)
        
    my_order.print_order()

    my_order.print_order()
    cost = my_order.order_cost()
    tax = round(my_order.order_tax(), 2)
    total_cost = round(cost + tax, 2)
    total = my_order.__len__()

    print("_____________________________________________________")
    print(f'Total number of items in order: {total}')
    print(f'Order Subtotals:                        {cost}     {tax}')
    print(f'Order Total:                                     {total_cost}')
    # print("Name        Quantity      Price         Cost     Tax")
    print("_____________________________________________________") 


if __name__ == "__main__":
    main()