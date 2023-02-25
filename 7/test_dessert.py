from dessertshop import *
from freezer import *
from dessert import *

#Test the datatype for DessertItems
def datatype(x):
    myfood = Candy(x, 1.2, 2.5)
    return myfood.name
def test_datatype():
    assert datatype('cake') == 'cake'

#Test Candy
def checkweight(x):
    mycandy = Candy('chupa', 1.3, 2.5)
    mycandy.candy_weight += x
    return mycandy.candy_weight

def test_checkweight():
    assert checkweight(1.3) == 2.6

def checkprice(x):
    mycandy = Candy('chupa', 1.3, 2.5)
    mycandy.price_per_pound += x
    return mycandy.price_per_pound

def test_checkprice():
    assert checkprice(1.3) == 3.8 

def checktotalprice(x):
    mycandy = Candy('godiva', 1, x)
    return mycandy.calculate_cost()

def test_checktotalprice():
    assert checktotalprice(100) == 100

def taxes(x):
    mycandy = Candy('godiva', 1, x)
    return mycandy.calculate_tax()

def check_taxes():
    assert taxes(100) == .75  
    
#test cookie 
def number_of_cookies(x):
    mycookie = Cookie('cookie', 3, 6.5)
    mycookie.cookie_quantity = mycookie.cookie_quantity + x
    return mycookie.cookie_quantity

def test_number_of_cookies():
    assert number_of_cookies(3) == 6

def cookieprice(x):
    mycookie = Cookie('cookie', 3, 6.5)
    mycookie.price_per_dozen += x
    return mycookie.price_per_dozen

def test_cookieprice():
    assert cookieprice(6.5) == 13.0

def checkcookieprice(x):
    mycookie = Cookie('cookies', 12, x)
    return mycookie.calculate_cost()

def test_checkcookieprice():
    assert checkcookieprice(10) == 10

def checkcookietax(x):
    mycookie = Cookie('cokies', 12, x)
    return mycookie.calculate_tax()

def test_checkcookietax():
    assert checkcookietax(100) == 7.25

#icecream
def countscoops(x):
    mycone = IceCream('ice', 3, .5)
    mycone.scoop_count += x
    return mycone.scoop_count

def test_scoops():
    assert countscoops(1) == 4

def checkprice(x):
    mycone1 = IceCream('ice', 3, 1.5)
    mycone1.price_per_scoop += x
    return mycone1.price_per_scoop

def test_checkprice():
    assert checkprice(2.5) == 4.0

def calc_icecream_price(x):
    mycone = IceCream('vanilla', 10, x)
    return mycone.calculate_cost()

def test_calc_icecream_price():
    assert calc_icecream_price(10) == 100

def icecream_tax_check(x):
    mycone = IceCream('vanilla', 10, x)
    return mycone.calculate_tax()

def test_icecream_tax_check():
    assert icecream_tax_check(10) == 7.25

#sudae
def sundaetopping(x):
    mysundae = Sundae('sundae', 2, 2.24, x, .75)
    return mysundae.topping_name

def test_sundaetopping():
    sundaetopping('topping') == 'topping'

def pricecheck(x):
    mysundae = Sundae('sundae', 2, 2.24, x, .75)
    mysundae.topping_price += x
    return mysundae.topping_price

def test_pricecheck():
    assert pricecheck(1) == 1.75

def calculate_sundae_price(x):
    mysundae = Sundae('topping1', 10, 9, 'sundae', x)
    return mysundae.calculate_cost()

def test_calculate_sundae_price():
    assert calculate_sundae_price(10) == 100

def calculate_sundae_tax(x):
    mysundae = Sundae('topping1', 10, 9, 'sundae', x)
    return mysundae.calculate_tax()

def test_calculate_sundae_tax():
    assert calculate_sundae_tax(10) == 7.25

#Test freeze 
def check_chill():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie.chill()
    return mycookie._temperature

def test_check_freeze():
    assert check_chill() == "chilling"

def check_thaw():
    mycookie = Cookie('Chocolate Chip', 3, 5.5)
    mycookie.thaw()
    return mycookie._temperature

def test_check_thaw():
    assert check_thaw() == "thawing"

#thaw for icecream
def check_chill():
    myicecream = IceCream('ice', 3, .5)
    myicecream.chill()
    return myicecream._temperature

def test_check_freeze():
    assert check_chill() == "chilling"

def check_thaw():
    myicecream = IceCream('ice', 3, .5)
    myicecream.thaw()
    return myicecream._temperature

def test_check_thaw():
    assert check_thaw() == "thawing"

#thaw for sundae
def check_chill():
    mysundae = Sundae('3 scoop sundae', 2, 2.24, 'sprinkles', .75)
    mysundae.chill()
    return mysundae._temperature

def test_check_freeze():
    assert check_chill() == "chilling"

def check_thaw():
    mysundae = Sundae('3 scoop sundae', 2, 2.24, 'sprinkles', .75)
    mysundae.thaw()
    return mysundae._temperature

def test_check_thaw():
    assert check_thaw() == "thawing"
