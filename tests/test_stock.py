import unittest
from stock_exchange.stock import create_stock, sell, buy

class TestStockFunctions(unittest.TestCase):
    def setUp(self):
        self.stock = create_stock(symbol='ABC')

    def test_create_stock(self):
        self.assertEqual(self.stock['symbol'], 'ABC')
        self.assertEqual(self.stock['value'], 1)
        self.assertEqual(self.stock['total_shares'], 100)
        self.assertEqual(self.stock['sold_shares'], 0)

    def test_sell(self):
        self.stock['sold_shares'] = 100
        sell(self.stock, 100)

        self.assertEqual(self.stock['sold_shares'], 0)

    def test_sell_fail(self):
        self.assertRaises(Exception, sell, self.stock, 100)

    def test_buy(self):
        buy(self.stock, 100)

        self.assertEqual(self.stock['sold_shares'], 100)

    def test_buy_fail(self):
        self.assertRaises(Exception, buy, self.stock, 200)
