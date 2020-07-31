# wstradepyapp
Unofficial Desktop App For Wealth Simple Trade

## Software Used

* Python 3
* PyQt5 https://pypi.org/project/PyQt5/
* requests https://pypi.org/project/requests/

## Background

Currently, WealthSimple Trade only has a mobile app. This projects aims to create an (unofficial) Desktop App to allow WealthSimple Trade to be used on Windows and Linux platforms.

## Screenshots

App development is currently a work in Progress.

![](docs/app.PNG)


## API documentation

Unoffical API documentation can be found here:

https://github.com/MarkGalloway/wealthsimple-trade/

## API tests

```bash
# use following curl command to get access token -> set EMAIL and PASSWORD
curl -i -H "Content-Type: application/json" -X POST -d "{\"email\": \"${EMAIL}\", \"password\": \"${PASSWORD}\"}" "https://trade-service.wealthsimple.com/auth/login"

# example tokens
ACCESS_TOKEN="SSDFASDASddfhdfgsdfawsd"
REFRESH_TOKEN="sdfsfdhdsfiasdhasdkjlasdkhjasd"

# get account balances
curl -H "Authorization: ${ACCESS_TOKEN}" "https://trade-service.wealthsimple.com/account/list"
curl -i -XPOST -d "{\"refresh_token\": \"${REFRESH_TOKEN}\"}" "https://trade-service.wealthsimple.com/auth/refresh"
```