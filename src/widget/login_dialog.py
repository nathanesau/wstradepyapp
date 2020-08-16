from PyQt5.QtWidgets import QDialog, QLineEdit, QGridLayout, QGroupBox, \
    QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon

from src.widget.ws_message_box import WSMessageBox

class LoginDialog(QDialog):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon(":icon.svg"))
        self.resize(300, 150)

        self.email_line_edit = QLineEdit()
        self.email_line_edit.setPlaceholderText("youremail@gmail.com")
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setPlaceholderText("yourpassword")
        self.credentials_layout = QGridLayout()
        self.credentials_layout.addWidget(QLabel("Email: "), 1, 1)
        self.credentials_layout.addWidget(self.email_line_edit, 1, 2)
        self.credentials_layout.addWidget(QLabel("Password: "), 2, 1)
        self.credentials_layout.addWidget(self.password_line_edit, 2, 2)
        self.credentials_group_box = QGroupBox("Credentials")
        self.credentials_group_box.setLayout(self.credentials_layout)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login_to_trade)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.login_button)
        self.button_layout.addWidget(self.cancel_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.credentials_group_box)
        self.main_layout.addStretch(1)
        self.main_layout.addLayout(self.button_layout)

        self.setLayout(self.main_layout)

    def login_to_trade(self):
        email = self.email_line_edit.text()
        password = self.password_line_edit.text()
        credentials = {"email": email, "password": password}
        status_code = self.api.login_to_trade(credentials)
        if status_code == 200:
            msg = WSMessageBox("Login was successful")
            msg.exec()
            self.parent().refresh_active_widget()
            self.accept()
        else:
            msg = WSMessageBox("Login was unsuccessful")
            msg.exec()
            self.parent().refresh_active_widget()
            self.reject()
