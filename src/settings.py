# part of wstradepyapp - backend

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

ORGANIZATION_NAME = "Unofficial"
APPLICATION_NAME = "WealthsimpleTradeDesktop"

class Settings:
    @staticmethod
    def get_credentials():
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        settings.beginGroup("Credentials")
        login_date = settings.value("login_date", None)
        access_token = settings.value("access_token", None)
        refresh_token = settings.value("refresh_token", None)
        first_name = settings.value("first_name", None)
        last_name = settings.value("last_name", None)
        email = settings.value("email", None)
        settings.endGroup()

        return {
            "login_date": login_date,
            "access_token": access_token,
            "refresh_token": refresh_token,
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }

    @staticmethod
    def set_credentials(credentials: dict):
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        settings.beginGroup("Credentials")
        if "login_date" in credentials:
            settings.setValue("login_date", credentials.get("login_date"))
        if "access_token" in credentials:
            settings.setValue("access_token", credentials.get("access_token"))
        if "refresh_token" in credentials:
            settings.setValue("refresh_oken", credentials.get("refresh_token"))
        if "first_name" in credentials:
            settings.setValue("first_name", credentials.get("first_name"))
        if "last_name" in credentials:
            settings.setValue("last_name", credentials.get("last_name"))
        if "email" in credentials:
            settings.setValue("email", credentials.get("email"))
        settings.endGroup()
        