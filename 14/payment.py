from enum import Enum


class PayType(Enum):
    CASH = 1
    CARD = 2
    PHONE = 3


class Payment:
    def __init__(self, pay_type: PayType):
        self.pay_type = pay_type

    @property
    def pay_type(self):
        return self._pay_type

    @pay_type.setter
    def pay_type(self, value: PayType):
        self._pay_type = value

    def __str__(self):
        return "{}".format(self.pay_type.name)