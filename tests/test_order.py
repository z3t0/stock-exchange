import unittest
from unittest.mock import Mock
from stock_exchange.Order import Order, OrderStatus

class TestOrderMethods(unittest.TestCase):
    def setUp(self):
        self.profile = Mock()
        self.stock = Mock()

        self.order = Order(self.profile, self.stock, 'buy', 100)

    def test_init(self):
        self.assertEqual(self.order.profile, self.profile)
        self.assertEqual(self.order.stock, self.stock)
        self.assertEqual(self.order.order_type, 'buy')
        self.assertEqual(self.order.shares, 100)
        self.assertEqual(self.order.status, OrderStatus.NOT_PROCESSED)

    def test_value(self):
        self.stock.value = 10
        expected_value = self.stock.value * self.order.shares

        self.assertEqual(self.order.value(), expected_value)

    # def test_process(self):
    #     self.stock.buy = Mock()
    #     self.profile.buy = Mock()

    #     self.order.process()

    #     self.stock.buy.assert_called_with(self.order)
    #     self.profile.buy.assert_called_with(self.order)

    #     self.assertEqual(self.order.status, OrderStatus.SUCCEEDED)

    # def test_process_fail(self):
    #     def error():
    #         raise Exception()

    #     self.stock.buy = Mock(side_effect=error)
    #     self.profile.buy = Mock(side_effect=error)

    #     self.order.process()

    #     self.stock.buy.assert_called_with(self.order)
    #     self.profile.buy.assert_called_with(self.order)

    #     #self.assertRaises(Exception, self.order.process)
    #     #self.assertEqual(self.order.status, OrderStatus.FAILED)
