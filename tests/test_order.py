import unittest
from unittest.mock import Mock
from stock_exchange.order import create_order


# class TestStockFunctions(unittest.TestCase):
    # def setUp(self):
    #     self.stock = Mock()
    #     self.profile = Mock()
    #     self.order = create_order(symbol='ABC', shares=100, order_type='buy',
    #                               profile='unique')

    # def test_create_order(self):
    #     self.assertEqual(self.order['symbol'], 'ABC')
    #     self.assertEqual(self.order['shares'], 100)
    #     self.assertEqual(self.order['order_type'], 'buy')
    #     self.assertEqual(self.order['profile'], 'unique')

    # def test_process(self):
    #     # Mock stock exchange
    #     def get_stock(symbol):
    #         return self.stock

    #     def get_profile(profile):
    #         return self.profile

    #     self.order.process()

    #     self.assertEqual(self.stock['sold_shares'], 100)
    #     self.assertEqual(self.
