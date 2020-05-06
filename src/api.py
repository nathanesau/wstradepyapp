import requests

# https://github.com/MarkGalloway/wealthsimple-trade/blob/master/API.md
class WealthsimpleTradeAPI:
    # auth: dictionary of username and password
    def __init__(self, auth):
        self.baseUrl = "https://trade-service.wealthsimple.com/auth/login"
        self.auth = auth

        self.loginData = None # login_to_trade

    def login_to_trade(self) -> int:
        r = requests.post(self.baseUrl, data=self.auth)
        try:
            self.loginData = r.json()
        except:
            print("Unable to retrieve JSON info from WS server")
        return r.status_code
