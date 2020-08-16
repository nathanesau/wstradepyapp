"""
WealthSimple Trade Python Application
"""
import sys
from PyQt5.QtWidgets import QApplication

from src.widget import MainWindow
from src.api import WealthsimpleTradeAPI

# pyrcc5 resources.qrc -o qrc_resources.py
# pylint: disable=W0611
from src import qrc_resources

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # backend
    api = WealthsimpleTradeAPI()

    # frontend (has reference to api)
    mainWindow = MainWindow(api)
    mainWindow.show()

    app.exec()
