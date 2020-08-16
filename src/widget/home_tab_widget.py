from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QScrollArea, \
    QVBoxLayout
from PyQt5.QtCore import Qt

from src.widget.account_list_widget import AccountListWidget
from src.widget.tab_widget import TabWidget

class HomeTabWidget(TabWidget):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, api, parent=None):
        super().__init__(api, parent)

        self.active = False

        self.info_label = QLabel()
        self.info_label.setText("Home")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")

        self.accounts_label1 = QLabel()
        self.accounts_label1.setText("Account List 1")
        self.accounts_label1.setStyleSheet("font-size: 10pt; font-weight: bold")

        self.accounts_label2 = QLabel()
        self.accounts_label2.setText("Account List 2")
        self.accounts_label2.setStyleSheet("font-size: 10pt; font-weight: bold")

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        self.balances_label = QLabel()

        self.accounts_widget1 = AccountListWidget(self.api)
        self.accounts_scroll_area1 = QScrollArea()
        self.accounts_scroll_area1.setWidgetResizable(True)
        self.accounts_scroll_area1.setAlignment(Qt.AlignCenter)
        self.accounts_scroll_area1.setWidget(self.accounts_widget1)

        self.accounts_widget2 = AccountListWidget(self.api)
        self.accounts_scroll_area2 = QScrollArea()
        self.accounts_scroll_area2.setWidgetResizable(True)
        self.accounts_scroll_area2.setAlignment(Qt.AlignCenter)
        self.accounts_scroll_area2.setWidget(self.accounts_widget2)

        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.accounts_label1)
        self.main_layout.addWidget(self.accounts_scroll_area1)
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.accounts_label2)
        self.main_layout.addWidget(self.accounts_scroll_area2)

        self.setLayout(self.main_layout)

    def refresh(self):
        # rebuild account list widget
        self.accounts_widget1.refresh()
        self.accounts_widget2.refresh()
        self.login_label.setText(self.get_login_label_text())

        self.repaint()
