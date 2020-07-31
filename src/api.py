# part of wstradepyapp - backend

import requests
from datetime import datetime
from src import constants
from src.settings import Settings

# https://github.com/MarkGalloway/wealthsimple-trade/blob/master/API.md
class WealthsimpleTradeAPI:

    def __init__(self):
        self.base_url = "https://trade-service.wealthsimple.com"
        self.authenticated = False
        self.login_date = None
        self.access_token = None
        self.refresh_token = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.authenticated = None
        self.read_from_settings()

    def read_from_settings(self):
         if constants.CACHE_CREDENTIALS:
            credentials = Settings.get_credentials()
            self.login_date = credentials.get("login_date", None)
            self.access_token = credentials.get("access_token", None)
            self.refresh_token = credentials.get("refresh_token", None)
            self.first_name = credentials.get("first_name", None)
            self.last_name = credentials.get("last_name", None)
            self.email = credentials.get("email", None)
            self.authenticated = self.access_token != None
            
    def write_to_settings(self):
        if constants.CACHE_CREDENTIALS:
            Settings.set_credentials({
                "login_date": self.login_date,
                "access_token": self.access_token,
                "refresh_token": self.refresh_token,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email
            })

    def clear_credentials(self):
        self.login_date = None
        self.access_token = None
        self.refresh_token = None
        self.first_name = None
        self.last_name = None
        self.email = None
        self.authenticated = False
        self.write_to_settings()

    def is_authenticated(self):
        # authenticated if has token and token valid (not expired)
        return self.authenticated

    def has_access_token(self):
        return self.access_token != None

    def get_login_name(self):
        return "{firstName} {lastName} <{email}>".format(
            firstName=self.first_name, lastName=self.last_name,
            email=self.email)

    # /auth/login -> return HTTP code
    def login_to_trade(self, credentials) -> int:
        url = "{}/auth/login".format(self.base_url)
        r = requests.post(url, data=credentials)
        try:
            headers = r.headers
            data = r.json()
            self.login_date = datetime.now()
            self.access_token = headers.get("x-access-token")
            self.refresh_token = headers.get("x-refresh-token")
            self.first_name = data.get("first_name")
            self.last_name = data.get("last_name")
            self.email = data.get("email")
            self.authenticated = (r.status_code == 200)
            self.write_to_settings()
        except:
            print("Unable to retrieve login info from WS server")
        return r.status_code

    # /account/list -> return json if successful else ""
    def get_accounts(self) -> str:
        url = "{}/account/list".format(self.base_url)
        headers = {'Authorization': self.access_token}
        r = requests.get(url, headers = headers)
        code = r.status_code

        if code != 200: # unauthorized access
            if code == 401 or code == 403:
                self.authenticated = False
            return ""

        data = r.json()
        return data.get("results")

    # /orders
    def get_orders(self):
        url = "{}/orders".format(self.base_url)
        headers = {'Authorization': self.access_token}
        r = requests.get(url, headers = headers)
        code = r.status_code

        if code != 200: # unauthorized access
            if code == 401 or code == 403:
                self.authenticated = False
            return None

        data = r.json()
        return data

    # TODO