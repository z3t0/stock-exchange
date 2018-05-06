import unittest
from stock_exchange.stock import Stock

stock = Stock('ABC', 1)

class TestStockMethods(unittest.TestCase):

    def test_init(self):
        self.assertEqual(stock.symbol, 'ABC')
        self.assertEqual(stock.value, 1)
        self.assertEqual(stock.order_history, [])
        self.assertEqual(stock.total_shares, 100)

        # should be 0, but is 100
        self.assertEqual(stock.sold_shares, 0)

    def test_buy(self):
        stock.buy(100)

        # sets it to 100
        self.assertEqual(stock.sold_shares, 100)

    # def test_sell(self):
    #     stock.sell(100)

    #     self.assertEqual(stock.sold_shares, 0)



if __name__ == '__main__':
    unittest.main()
