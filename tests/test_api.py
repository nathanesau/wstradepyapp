import unittest
import sys
from src import api
from src import data

try:
    # put credentials in tests/config.py that shouldn't be checked in
    from tests.config import EMAIL, PASSWORD, NON_TFSA_ID
except:
    # no email, password available
    EMAIL = None
    PASSWORD = None
    NON_TFSA_ID = None

# set email and password temporarily if you want to run tests
class TestWealthsimpleTradeAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        credentials = {
            "email": EMAIL,
            "password": PASSWORD
        }
        cls.api = api.WealthsimpleTradeAPI()
        cls.api.login_to_trade(credentials)

    @unittest.skipIf(EMAIL == None or PASSWORD is None, "no credentials available")
    def test_get_accounts(self):
        accounts = self.api.get_accounts()
        account_list = data.get_account_list(accounts)
        self.assertTrue(accounts != None)

    @unittest.skipIf(EMAIL == None or PASSWORD is None, "no credentials available")
    def test_get_orders(self):
        orders = self.api.get_orders()
        self.assertTrue(orders != None)

    @unittest.skipIf(EMAIL == None or PASSWORD is None, "no credentials available")
    def test_get_positions(self):
        positions = self.api.get_positions()
        position_list = data.get_positions_list(positions)
        self.assertTrue(positions != None)