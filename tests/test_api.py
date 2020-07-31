import unittest
import sys
from src import api

# set email and password temporarily if you want to run tests
class TestWealthsimpleTradeAPI(unittest.TestCase):
    EMAIL = None
    PASSWORD = None

    @classmethod
    def setUpClass(cls):
        credentials = {
            "email": TestWealthsimpleTradeAPI.EMAIL,
            "password": TestWealthsimpleTradeAPI.PASSWORD
        }
        cls.api = api.WealthsimpleTradeAPI()
        cls.api.login_to_trade(credentials)

    @unittest.skipIf(EMAIL == None or PASSWORD is None, "no credentials available")
    def test_get_account_balances(self):
        accounts = self.api.get_accounts()
        self.assertTrue(accounts != None)

    @unittest.skipIf(EMAIL == None or PASSWORD is None, "no credentials available")
    def test_get_orders(self):
        orders = self.api.get_orders()
        self.assertTrue(orders != None)