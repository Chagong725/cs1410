from dessertshop import Customer

#Tests for Customer class

def test_customer_name():
    newcustomer = Customer('Lance')
    assert newcustomer.name == 'Lance'

def test_customer_class():
    newcustomer = Customer('Lance')
    assert isinstance(newcustomer, Customer)