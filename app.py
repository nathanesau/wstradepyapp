from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import sys

from src.widgets import MainWindow
from src.api import WealthsimpleTradeAPI

# pyrcc5 resources.qrc -o qrc_resources.py
from src import qrc_resources

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # backend
    api = WealthsimpleTradeAPI()

    # frontend (has reference to api)
    mainWindow = MainWindow(api)
    mainWindow.show()

    app.exec()
