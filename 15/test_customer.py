import uuid
from typing import Dict

import dessertshop
import test_dessert


def add_customer_to_db(customer_name: str, customer_db: Dict[str, dessertshop.Customer]) -> None:
    if customer_name not in customer_db:
        customer = dessertshop.Customer(customer_name)
        customer_db[customer_name] = customer
    else:
        customer = customer_db[customer_name]
    return customer.customer_id


def test_customer_attributes():
    customer = dessertshop.Customer("Jaren")
    assert customer.customer_name == "Jaren"
    assert customer.order_history == []
    assert isinstance(customer.customer_id, int)


def test_add2history():
    customer = dessertshop.Customer("Jaren")
    order = test_dessert.new_Order()
    customer.add2history(order)
    assert customer.order_history[0] == order
    assert len(customer.order_history) == 1


def test_customer_id():
    customer_db: Dict[str, dessertshop.Customer] = {}
    customer_1 = "Jaren"
    customer_2 = "Elli"
    assert add_customer_to_db(customer_1, customer_db) == add_customer_to_db("Jaren", customer_db)
    assert add_customer_to_db(customer_2, customer_db) == add_customer_to_db("Elli", customer_db)
    assert not add_customer_to_db(customer_1, customer_db) == add_customer_to_db(customer_2, customer_db)
