from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import requests
import sys

import constants
import qrc_resources
import widgets

if __name__ == "__main__":
     app = QApplication(sys.argv)

     mainWindow = widgets.MainWindow()
     mainWindow.show()

     app.exec()
