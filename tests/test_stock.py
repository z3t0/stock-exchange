import unittest
from stock_exchange.stock import Stock

stock = Stock('ABC', 1)

class TestStockMethods(unittest.TestCase):

    def test_init(self):
        self.assertEqual(stock.symbol, 'ABC')
        self.assertEqual(stock.value, 1)

    def test_set_value(self):
        stock.set_value(2)
        self.assertEqual(stock.value, 2)

if __name__ == '__main__':
    unittest.main()
