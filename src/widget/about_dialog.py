from PyQt5.QtWidgets import QDialog, QLabel, QHBoxLayout, QVBoxLayout, \
    QPushButton
from PyQt5.QtGui import QIcon

from src import constants

class AboutDialog(QDialog):
    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        self.info_label = QLabel()
        self.info_label.setText("Name: {}".format(constants.APP_NAME))
        self.version_label = QLabel()
        self.version_label.setText("Version: {}".format(constants.VERSION))

        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.button_layout = QHBoxLayout()
        self.button_layout.addStretch(1)
        self.button_layout.addWidget(self.ok_button)
        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.info_label)
        self.main_layout.addWidget(self.version_label)
        self.main_layout.addLayout(self.button_layout)
        self.setLayout(self.main_layout)

        self.setWindowTitle("About")
        self.setWindowIcon(QIcon(":icon.svg"))
        self.resize(200, 100)
