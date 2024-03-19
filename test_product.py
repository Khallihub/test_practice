
import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_init(self):
        product = Product('apple', 10, 5)
        self.assertEqual(product.name, 'apple')
        self.assertEqual(product.price, 10)
        self.assertEqual(product.quantity, 5)
        
        self.assertEqual(type(product.name), str)
        self.assertEqual(type(product.price), int)
        self.assertEqual(type(product.quantity), int)

    def test_negative_input(self):

        with self.assertRaises(ValueError):
            Product('apple', 5, -5)
    
    def test_calculateTotal(self):
        product = Product('apple', 10, 5)
        self.assertEqual(product.calculateTotal(), 50)

    def test_calcualteTotal_with_zero_quantity(self):
        product = Product('apple', 10, 0)
        self.assertEqual(product.calculateTotal(), 0)


if __name__ == '__main__':
    unittest.main()

