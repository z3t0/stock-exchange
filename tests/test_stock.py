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

    def test__sell(self):
        sell = 100
        self.stock.sold_shares = sell

        self.stock._sell(sell)
        self.assertEqual(self.stock.sold_shares, 0)

    def test__buy(self):
        buy = 100
        
        self.stock._buy(buy)
        self.assertEqual(self.stock.sold_shares, buy)

