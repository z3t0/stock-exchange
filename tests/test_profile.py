import unittest
from unittest.mock import Mock

from stock_exchange.profile import create_profile, buy, sell
from uuid import UUID


class TestProfileFunction(unittest.TestCase):
    def setUp(self):
        self.profile = create_profile()

    def test_create_profile(self):
        self.assertIsInstance(self.profile['uuid'], UUID)
        self.assertEqual(self.profile['cash'], 100)
        self.assertEqual(self.profile['assets'], {})

    def test_buy_existing(self):
        self.profile['assets']['ABC'] = {'shares': 10}

        buy(self.profile, symbol='ABC', shares=100, cost=10)

        self.assertEqual(self.profile['assets']['ABC']['shares'],
                         110)

        self.assertEqual(self.profile['cash'], 90)

    def test_buy_new(self):
        buy(self.profile, symbol='ABC', shares=100, cost=10)

        self.assertEqual(self.profile['assets']['ABC']['shares'],
                         100)

        self.assertEqual(self.profile['cash'], 90)

    def test_buy_fail(self):
        self.profile['assets']['ABC'] = {'shares': 10}
        self.assertRaises(Exception, buy, self.profile, symbol='ABC',
                          shares=100, cost=1000)

        self.assertEqual(self.profile['assets']['ABC']['shares'],
                         10)

        self.assertEqual(self.profile['cash'], 100)

    def test_sell_existing(self):
        self.profile['assets']['ABC'] = {'shares': 10}

        sell(self.profile, symbol='ABC', shares=10, cost=10)

        self.assertEqual(self.profile['assets']['ABC']['shares'],
                         0)

        self.assertEqual(self.profile['cash'], 110)

    def test_sell_fail_does_not_exist(self):
        self.profile['assets']['ABC'] = {'shares': 10}

        self.assertRaises(Exception, sell, self.profile, symbol='ABC',
                          shares=20, cost=10)

        self.assertEqual(self.profile['assets']['ABC']['shares'],
                         10)

        self.assertEqual(self.profile['cash'], 100)

    def test_sell_fail_not_enough_cash(self):
        self.assertRaises(Exception, sell, self.profile, symbol='ABC',
                          shares=20, cost=10)

        self.assertEqual(self.profile['cash'], 100)
