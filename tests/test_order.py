import unittest
from unittest.mock import Mock
from stock_exchange.Order import Order

profile = Mock()
stock = Mock()
order = Order(profile, stock, 'buy', 100)

class TestOrderMethods(unittest.TestCase):

    def test_init(self):
        self.assertEqual(order.profile, profile)
        self.assertEqual(order.stock, stock)
        self.assertEqual(order.order_type, 'buy')
        self.assertEqual(order.shares, 100)
        self.assertEqual(order.processed, False)
        self.assertEqual(order.succeeded, False)

if __name__ == '__main__':
    unittest.main()
