import unittest
from stock_exchange.stock import Stock

stock = Stock('ABC', 1)

class TestStockMethods(unittest.TestCase):

    def test_init(self):
        self.assertEqual(stock.symbol, 'ABC')
        self.assertEqual(stock.value, 1)
        self.assertEqual(stock.order_history, [])
        self.assertEqual(stock.total_shares, 100)

if __name__ == '__main__':
    unittest.main()
