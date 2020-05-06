from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

ORGANIZATION_NAME = "nathanesau_software"
APPLICATION_NAME = "WealthsimpleTradeDesktop"

class Settings:
    @staticmethod
    def getEmail():
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        settings.beginGroup("Credentials")
        email = settings.value("email", "myemail@gmail.com")
        settings.endGroup()
        return email

    @staticmethod
    def setEmail(email):
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        settings.beginGroup("Credentials")
        settings.setValue("email", email)
        settings.endGroup()

    @staticmethod
    def getPassword():
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        settings.beginGroup("Credentials")
        password = settings.value("password", "mypassword")
        settings.endGroup()
        return password

    @staticmethod
    def setPassword(password):
        settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        settings.beginGroup("Credentials")
        settings.setValue("password", password)
        settings.endGroup()
