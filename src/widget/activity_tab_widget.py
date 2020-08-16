from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout

from src.widget.tab_widget import TabWidget

class ActivityTabWidget(TabWidget):
    def __init__(self, api, parent=None):
        super().__init__(api, parent)

        self.active = False

        self.info_label = QLabel()
        self.info_label.setText("Activity")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        self.login_label.setText(self.get_login_label_text())
        self.repaint()
