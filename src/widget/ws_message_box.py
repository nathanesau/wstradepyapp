from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class WSMessageBox(QMessageBox):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setWindowIcon(QIcon(":icon.svg"))
        self.setWindowTitle("Info")
