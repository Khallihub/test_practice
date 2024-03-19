import unittest

class Product:
    def __init__(self, name, price, quantity) -> None:
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculateTotal(self):
        if self.quantity < 0 or self.price < 0:
            raise ValueError('Price and quantity must be greater than 0')
        return self.price * self.quantity
    






