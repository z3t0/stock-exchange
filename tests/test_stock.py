import unittest
from unittest.mock import Mock
from stock_exchange.stock import Stock

class TestStockMethods(unittest.TestCase):

    def setUp(self):
        self.stock = Stock('ABC', 1)
        self.order = Mock()

    def test_init(self):
        self.assertEqual(self.stock.symbol, 'ABC')
        self.assertEqual(self.stock.value, 1)
        self.assertEqual(self.stock.order_history, [])
        self.assertEqual(self.stock.total_shares, 100)
        self.assertEqual(self.stock.sold_shares, 0)

    def test_buy(self):
        self.order.shares = 100


        self.stock.buy(self.order)

        self.assertEqual(self.stock.sold_shares, 100)
        self.assertEqual(self.stock.order_history[-1], self.order)

    def test_buy_fail(self):
        self.order.shares = 100
        self.assertRaises(Exception, self.stock.buy, 200)
        self.assertEqual(len(self.stock.order_history), 0)

    def test_sell(self):
        self.order.shares = 100

        # So that shares can be sold
        self.stock.sold_shares = 100

        self.stock.sell(self.order)

        self.assertEqual(self.stock.sold_shares, 0)
        self.assertEqual(self.stock.order_history[-1], self.order)

    def test_sell_fail(self):
        self.order.shares = 100
        self.assertRaises(Exception, self.stock.sell, self.order)

    def test_buy_fail(self):
        self.order.shares = 200
        self.assertRaises(Exception, self.stock.buy, self.order)
