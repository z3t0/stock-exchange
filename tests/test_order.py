import unittest
from unittest.mock import Mock
from stock_exchange.Order import Order

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
        self.assertEqual(self.order.processed, False)
        self.assertEqual(self.order.succeeded, False)

    def test_value(self):
        self.stock.value = 10
        expected_value = self.stock.value * self.order.shares

        self.assertEqual(self.order.value(), expected_value)

    # def test_process(self):
        # order.process()

if __name__ == '__main__':
    unittest.main()
