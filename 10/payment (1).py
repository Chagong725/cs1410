from enum import Enum

class Payment(Enum):
    Cash = 1
    Card = 2
    Phone = 3

    def payment_method(self):
        return self.name