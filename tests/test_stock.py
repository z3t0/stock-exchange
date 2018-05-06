import unittest
from stock_exchange.stock import Stock

class TestStockMethods(unittest.TestCase):
    def test_get_symbol(self):
        stock = Stock('ABC', 1)
        self.assertEqual(stock.get_symbol(), 'ABC')

    def test_get_value(self):
        stock = Stock('ABC', 1)
        self.assertEqual(stock.get_value(), 1)

if __name__ == '__main__':
    unittest.main()
