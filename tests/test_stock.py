import unittest
from stock_exchange.stock import Stock

class TestStockMethods(unittest.TestCase):
    def test_symbol(self):
        stock = Stock('ABC', 1)
        self.assertEqual(stock.get_symbol(), 'ABC')

if __name__ == '__main__':
    unittest.main()
