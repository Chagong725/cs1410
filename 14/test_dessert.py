import dessert
from freeze import Freeze, Freezer
from payment import PayType, Payment

Candy = dessert.Candy
Cookie = dessert.Cookie
IceCream = dessert.IceCream
Sundae = dessert.Sundae
freezer = Freezer()
Order = dessert.Order


def new_Candy():
    return Candy("test candy", 1.50, 2.56)


def new_Cookie():
    return Cookie("test cookie", 12, 12.99)


def new_IceCream():
    return IceCream("test ice cream", 3, 1.99)


def new_Sundae():
    return Sundae("test sundae", 3, 1.59, "test topping", .59)


def new_Freezer():
    freezer.put(Cookie("Oatmeal Raisin Cookies"))
    freezer.put(Cookie("Chocolate Chip Cookies"))
    freezer.put(IceCream("Pistachio Ice Cream"))
    freezer.put(IceCream("Vanilla Ice Cream"))
    freezer.put(Sundae("Hot Fudge Topping"))
    return freezer


def new_Order():
    my_order = Order(PayType.CASH)
    my_order.add(new_Candy())
    my_order.add(new_Sundae())
    my_order.add(new_Cookie())
    my_order.add(new_IceCream())
    return my_order


def test_Order():
    new_order = new_Order()
    # testing constructor for default values
    assert new_order.get_payment_method() == "CASH"
    # testing constructor for non-default values
    new_order.set_pay_method(2)
    assert new_order.get_payment_method() == "CARD"
    # modifying attribute values for default values
    new_order.set_pay_method(3)
    assert new_order.get_payment_method() == "PHONE"


def test_RelationalOperations():
    cookie_1 = new_Cookie().price
    cookie_2 = new_Cookie().price
    candy = new_Candy().price
    assert cookie_1 == cookie_1
    assert cookie_1 == cookie_2
    assert not cookie_1 == candy

    assert not cookie_1 != cookie_1
    assert cookie_1 != candy
    assert not cookie_1 != cookie_2

    assert candy < cookie_1
    assert not cookie_1 < candy
    assert not cookie_1 < cookie_2

    assert not candy > cookie_1
    assert cookie_1 > candy
    assert not cookie_1 > cookie_2

    assert not candy >= cookie_1
    assert cookie_1 >= candy
    assert cookie_1 >= cookie_2

    assert not cookie_1 <= candy
    assert candy <= cookie_1
    assert cookie_1 <= cookie_2


def test_Freezer():
    new_freezer = new_Freezer()
    assert isinstance(new_freezer.items[0], Cookie)
    assert isinstance(new_freezer.items[1], Cookie)
    assert isinstance(new_freezer.items[2], IceCream)
    assert isinstance(new_freezer.items[3], IceCream)
    assert isinstance(new_freezer.items[4], Sundae)
    assert new_freezer.take("Oatmeal Raisin Cookies") == "Oatmeal Raisin Cookies"
    assert new_freezer.take("Pistachio Ice Cream") == "Pistachio Ice Cream"
    assert new_freezer.take("Hot Fudge Topping") == "Hot Fudge Topping"


def test_Candy():
    # testing constructor for default values
    candy = Candy()
    assert candy.name == ""
    assert candy.unit == float
    assert candy.price == float
    assert candy.tax_percent == 7.25
    assert candy.packaging == "Bag"
    # testing constructor for non-default values
    assert new_Candy().name == "test candy"
    assert new_Candy().price == 2.56
    assert new_Candy().unit == 1.5
    assert new_Candy().calculate_cost() == 3.84
    assert new_Candy().tax_percent == 7.25
    assert new_Candy().calculate_tax() == .2784
    # modifying attribute values for default values
    candy_mod = Candy()
    candy_mod.name = "Sweettarts"
    assert candy_mod.name == "Sweettarts"
    candy_mod.unit = "2.9"
    assert candy_mod.unit == "2.9"
    candy_mod.price = "1"
    assert candy_mod.price == "1"
    assert candy_mod.calculate_cost() == 2.9
    assert candy_mod.tax_percent == 7.25
    assert candy_mod.calculate_tax() == 0.21025
    # modifying attribute values for non-default values
    candy_mod2 = new_Candy()
    candy_mod2.name = "Twix"
    assert candy_mod2.name == "Twix"
    candy_mod2.unit = "3"
    assert candy_mod2.unit == "3"
    candy_mod2.price = "100"
    assert candy_mod2.price == "100"
    assert candy_mod2.calculate_cost() == 300
    assert candy_mod2.tax_percent == 7.25
    assert candy_mod2.calculate_tax() == 21.75
    candy_combine = Candy("Twix", "3", "1.5")
    candy_combine2 = Candy("Twix", "4", "1.5")
    cookie_combine = new_Cookie()
    assert candy_combine.can_combine(candy_combine2)
    candy_combine.combine(candy_combine2)
    assert candy_combine.unit == 7.0
    assert not candy_combine.can_combine(cookie_combine)
    assert not candy_combine.combine(cookie_combine)


def test_Cookie():
    # testing constructor for default values
    cookie = Cookie()
    assert cookie.name == " Cookies"
    assert cookie.unit == float
    assert cookie.price == float
    assert cookie.tax_percent == 7.25
    assert cookie.packaging == "Box"
    # testing constructor for non-default values
    assert new_Cookie().name == "test cookie Cookies"
    assert new_Cookie().price == 12.99
    assert new_Cookie().unit == 12
    assert new_Cookie().calculate_cost() == 12.99
    assert new_Cookie().tax_percent == 7.25
    assert new_Cookie().calculate_tax() == .9417749999999999
    # modifying attribute values for default values
    cookie_mod = Cookie()
    cookie_mod.name = "Chocolate Chip"
    assert cookie_mod.name == "Chocolate Chip"
    cookie_mod.unit = "6"
    assert cookie_mod.unit == "6"
    cookie_mod.price = "6.99"
    assert cookie_mod.price == "6.99"
    assert cookie_mod.calculate_cost() == 3.495
    assert cookie_mod.tax_percent == 7.25
    assert cookie_mod.calculate_tax() == .2533875
    # modifying attribute values for non-default values
    cookie_mod2 = new_Cookie()
    cookie_mod2.name = "Oreo"
    assert cookie_mod2.name == "Oreo"
    cookie_mod2.unit = 8
    assert cookie_mod2.unit == 8
    cookie_mod2.price = 10
    assert cookie_mod2.price == 10
    assert cookie_mod2.calculate_cost() == 6.666666666666667
    assert cookie_mod2.tax_percent == 7.25
    assert cookie_mod2.calculate_tax() == 0.48333333333333334
    new_freezer = new_Freezer()
    assert new_freezer.take(cookie.name) == " Cookies"
    assert new_freezer.take(cookie_mod.name) == "Chocolate Chip"
    assert new_freezer.take(cookie_mod2.name) == "Oreo"
    cookie_combine = Cookie("Chip",  "6", "8")
    cookie_combine2 = Cookie("Chip", "4", "8")
    candy_combine = new_Candy()
    assert cookie_combine.can_combine(cookie_combine2)
    cookie_combine.combine(cookie_combine2)
    assert cookie_combine.unit == 10.0
    assert not cookie_combine.can_combine(candy_combine)
    assert not cookie_combine.combine(candy_combine)


def test_IceCream():
    # testing constructor for default values
    ice_cream = IceCream()
    assert ice_cream.name == " Ice Cream"
    assert ice_cream.unit == float
    assert ice_cream.price == float
    assert ice_cream.tax_percent == 7.25
    assert ice_cream.packaging == "Bowl"
    # testing constructor for non-default values
    assert new_IceCream().name == "test ice cream Ice Cream"
    assert new_IceCream().price == 1.99
    assert new_IceCream().unit == 3
    assert new_IceCream().calculate_cost() == 5.97
    assert new_IceCream().tax_percent == 7.25
    assert new_IceCream().calculate_tax() == 0.43282499999999996
    # modifying attribute values for default values
    ice_cream_mod = IceCream()
    ice_cream_mod.name = "Chocolate Chip"
    assert ice_cream_mod.name == "Chocolate Chip"
    ice_cream_mod.unit = "6"
    assert ice_cream_mod.unit == "6"
    ice_cream_mod.price = "6.99"
    assert ice_cream_mod.price == "6.99"
    assert ice_cream_mod.calculate_cost() == 41.94
    assert ice_cream_mod.tax_percent == 7.25
    assert ice_cream_mod.calculate_tax() == 3.0406499999999994
    # modifying attribute values for non-default values
    ice_cream_mod2 = new_IceCream()
    ice_cream_mod2.name = "Vanilla"
    assert ice_cream_mod2.name == "Vanilla"
    ice_cream_mod2.unit = 8
    assert ice_cream_mod2.unit == 8
    ice_cream_mod2.price = 10
    assert ice_cream_mod2.price == 10
    assert ice_cream_mod2.calculate_cost() == 80.0
    assert ice_cream_mod2.tax_percent == 7.25
    assert ice_cream_mod2.calculate_tax() == 5.8
    new_freezer = new_Freezer()
    assert new_freezer.take(ice_cream.name) == " Ice Cream"
    assert new_freezer.take(ice_cream_mod.name) == "Chocolate Chip"
    assert new_freezer.take(ice_cream_mod2.name) == "Vanilla"


def test_Sundae():
    # testing constructor for default values
    sundae = Sundae()
    assert sundae.name == "  Sundae"
    assert sundae.unit == int
    assert sundae.price == float
    assert sundae.topping_name == ""
    assert sundae.topping_price == float
    assert sundae.packaging == "Boat"
    assert sundae.tax_percent == 7.25
    # testing constructor for non-default values
    assert new_Sundae().name == "test topping test sundae Sundae"
    assert new_Sundae().price == 1.59
    assert new_Sundae().unit == 3
    assert new_Sundae().topping_name == "test topping"
    assert new_Sundae().topping_price == .59
    assert new_Sundae().calculate_cost() == 5.36
    assert new_Sundae().tax_percent == 7.25
    assert new_Sundae().calculate_tax() == 0.3886
    # modifying attribute values for default values
    sundae_mod = Sundae()
    sundae_mod.name = "Chocolate"
    assert sundae_mod.name == "Chocolate"
    sundae_mod.unit = "6"
    assert sundae_mod.unit == "6"
    sundae_mod.price = "6.99"
    assert sundae_mod.price == "6.99"
    sundae_mod.topping_name = "Hot Fudge"
    assert sundae_mod.topping_name == "Hot Fudge"
    sundae_mod.topping_price = "1.99"
    assert sundae_mod.topping_price == "1.99"
    assert sundae_mod.calculate_cost() == 43.93
    assert sundae_mod.tax_percent == 7.25
    assert sundae_mod.calculate_tax() == 3.184925
    # modifying attribute values for non-default values
    sundae_mod2 = new_Sundae()
    sundae_mod2.name = "Vanilla"
    assert sundae_mod2.name == "Vanilla"
    sundae_mod2.unit = "8"
    assert sundae_mod2.unit == "8"
    sundae_mod2.price = "10"
    assert sundae_mod2.price == "10"
    sundae_mod2.topping_name = "Hot Fudge"
    assert sundae_mod2.topping_name == "Hot Fudge"
    sundae_mod2.topping_price = "1.99"
    assert sundae_mod2.topping_price == "1.99"
    assert sundae_mod2.calculate_cost() == 81.99
    assert sundae_mod2.tax_percent == 7.25
    assert sundae_mod2.calculate_tax() == 5.944274999999999
    new_freezer = new_Freezer()
    assert new_freezer.take(sundae.name) == "  Sundae"
    assert new_freezer.take(sundae_mod.name) == "Chocolate"
    assert new_freezer.take(sundae_mod2.name) == "Vanilla"


def test_dessert_item():
    candy = Candy("SweetRopes", 1.20, 2.30)
    assert candy.name == "SweetRopes"
    assert candy.unit == 1.2
    assert candy.price == 2.3
    assert candy.calculate_cost() == 2.76
    assert candy.tax_percent == 7.25
    assert candy.calculate_tax() == .20009999999999997