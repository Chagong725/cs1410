from dessertshop import Customer
import random
import string

#Customer class
def test_customer_name():
    newcustomer = Customer('Lance')
    assert newcustomer.name == 'Lance'

def test_customer_class():
    newcustomer = Customer('Lance')
    assert isinstance(newcustomer, Customer)

#Test that customerid is always unique
def test_customer_id():
    listostrings = []
    #generate random string
    N = 10
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    if res in listostrings:
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    else:
        listostrings.append(res)
    #list to store customer ids
    customerlist = []
    #generate 100 customers
    for i in range(100):
        newcustomer = Customer(res)
        newcustomer.figure_customerid(customerlist)
        customerlist.append(newcustomer.customerid)
    #check that all customer ids are unique by taking advantage of the fact that sets cannot contain duplicates
    assert len(customerlist) == len(set(customerlist))