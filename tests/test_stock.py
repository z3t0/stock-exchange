import unittest
from stock_exchange.stock import Stock

class TestStockMethods(unittest.TestCase):

    def setUp(self):
        self.stock = Stock('ABC', 1)

    def test_init(self):
        self.assertEqual(self.stock.symbol, 'ABC')
        self.assertEqual(self.stock.value, 1)
        self.assertEqual(self.stock.order_history, [])
        self.assertEqual(self.stock.total_shares, 100)
        self.assertEqual(self.stock.sold_shares, 0)

    def test_buy(self):
        self.stock.buy(100)

        self.assertEqual(self.stock.sold_shares, 100)

    def test_buy_fail(self):
        self.assertRaises(Exception, self.stock.buy, 200)
                                    

    def test_sell(self):
        # So that shares can be sold
        self.stock.sold_shares = 100 

        self.stock.sell(100)

        self.assertEqual(self.stock.sold_shares, 0)

    def test_sell_fail(self):
        self.assertRaises(Exception, self.stock.sell, 100)

if __name__ == '__main__':
    unittest.main()
