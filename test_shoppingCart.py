import unittest
from shoppingCart import ShoppingCart
from product import Product

class TestShoppingCart(unittest.TestCase):
    def test_getCartTotal_empyt(self):
        cart = ShoppingCart()
        total = cart.calculateTotal()
        self.assertEqual(total, 0)

    def test_getCartTotal_with_products(self):
        cart = ShoppingCart()
        cart.addProduct(Product('apple', 10, 5))
        cart.addProduct(Product('banana', 5, 5))

        total = cart.calculateTotal()
        self.assertEqual(total, 75)

    def test_addProduct(self):
        product = Product('apple', 10, 5)
        cart = ShoppingCart()
        cart.addProduct(product)

        self.assertEqual(cart.cart[-1], product)


    



if __name__ == '__main__':
    unittest.main()