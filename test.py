from unittest.case import _AssertRaisesBaseContext


class Product:
    def __init__(self,name,price,quantity):
        if price < 0 or quantity < 0:
            raise ValueError('Price and quantity cannot be negative')
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def calculateTotal(self):
        if self.price < 0 or self.quantity < 0:
            raise ValueError('Price and quantity cannot be negative')
        return self.price * self.quantity
    
class ShoppingCart:
    def __init__(self):
        self.cart = []
    
    def addProduct(self,product):
        self.cart.append(product)

    def getCartTotal(self):
        total = 0
        for product in self.cart:
            total += product.calculateTotal()
        return total
    
# unit test
def test_product():
    product = Product('Apple', 10, 3)
    assert product.calculateTotal() == 30
    product = Product('Orange', 20, -5)
    assert product.calculateTotal() == -100
    product = Product('Orange', -20, 5)
    assert product.calculateTotal() == -100
    print('All test cases passed!')

def test_shopping_cart():
    cart = ShoppingCart()
    # test for empty cart
    assert cart.getCartTotal() == 0
    # test for non empty cart
    product1 = Product('Apple', 10, 3)
    product2 = Product('Orange', 20, 5)
    cart.addProduct(product1)
    cart.addProduct(product2)
    assert cart.getCartTotal() == 130
    print('All test cases passed!')

def testCalculateTotalZeroQuantity():
    product = Product('Apple', 10, 0)
    assert product.calculateTotal() == 0
    print('All test cases passed!')

def testCalculateTotalNegativeQuantity():
    product = Product('Apple', 10, -3)
    with _AssertRaisesBaseContext(ValueError):
        product.calculateTotal()
    print('All test cases passed!')

test_product()
test_shopping_cart()
