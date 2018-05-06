import unittest
import stock_exchange.stock

class TestStockMethods(unittest.TestCase):
    def test_symbol(self):
        stock = Stock('ABC')
        self.assertEqual(stock.symbol(), 'ABC')

if __name__ == '__main__':
    unittest.main()
