from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import api
import constants
from settings import Settings

class WSMessageBox(QMessageBox):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setWindowIcon(QIcon(":icon.svg"))
        self.setWindowTitle("Info")

class WSAccountInfoWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.nameLabel = QLabel("N/A")
        self.userIDLabel = QLabel("N/A")

        self.infoLayout = QVBoxLayout()
        self.infoLayout.addWidget(self.nameLabel)
        self.infoLayout.addWidget(self.userIDLabel)
        self.infoGroupBox = QGroupBox("Account Info")
        self.infoGroupBox.setLayout(self.infoLayout)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.infoGroupBox)
        self.mainLayout.addStretch(1)
        self.setLayout(self.mainLayout)

    def populateAccountInfo(self):
        auth={"email": Settings.getEmail(), "password": Settings.getPassword() }
        wsAPI = api.WealthsimpleTradeAPI(auth=auth)
        r = wsAPI.login_to_trade()

        if r != 200:
            print("Unable to connect to WS server")
            return

        try:
            first_name = wsAPI.loginData["first_name"]
            self.nameLabel.setText(first_name)
            external_ws_user_id = wsAPI.loginData["external_ws_user_id"]
            self.userIDLabel.setText(external_ws_user_id)
        except:
            print("Unable to retrieve account info from WS server")
            return

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.preferencesAction = QAction("Preferences")
        self.preferencesAction.triggered.connect(self.onPreferences)

        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction(self.preferencesAction)

        self.accountInfoWidget = WSAccountInfoWidget()
        self.accountInfoWidget.populateAccountInfo()
        self.setCentralWidget(self.accountInfoWidget)

        self.setWindowTitle(constants.APP_NAME)
        self.setWindowIcon(QIcon(":icon.svg"))
        self.resize(500, 500)

    def onPreferences(self):
        dlg = PreferencesDialog(self)
        if dlg.exec():
            email = dlg.emailLineEdit.text()
            password = dlg.passwordLineEdit.text()
            Settings.setEmail(email)
            Settings.setPassword(password)
            WSMessageBox("Wrote email and password to settings file", self).exec()

class PreferencesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preferences")
        self.setWindowIcon(QIcon(":icon.svg"))
        self.resize(400, 400)

        self.emailLineEdit = QLineEdit()
        self.emailLineEdit.setText(Settings.getEmail())
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setText(Settings.getPassword())
        self.credentialsLayout = QGridLayout()
        self.credentialsLayout.addWidget(QLabel("Email: "), 1, 1)
        self.credentialsLayout.addWidget(self.emailLineEdit, 1, 2)
        self.credentialsLayout.addWidget(QLabel("Password: "), 2, 1)
        self.credentialsLayout.addWidget(self.passwordLineEdit, 2, 2)
        self.credentialsGroupBox = QGroupBox("Credentials")
        self.credentialsGroupBox.setLayout(self.credentialsLayout)

        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.accept)
        self.cancelButton = QPushButton("Cancel")
        self.cancelButton.clicked.connect(self.reject)
        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.okButton)
        self.buttonLayout.addWidget(self.cancelButton)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.credentialsGroupBox)
        self.mainLayout.addStretch(1)
        self.mainLayout.addLayout(self.buttonLayout)

        self.setLayout(self.mainLayout)