from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QScrollArea, \
    QVBoxLayout
from PyQt5.QtCore import Qt

from src.widget.positions_list_widget import PositionsListWidget
from src.widget.tab_widget import TabWidget

class PositionsTabWidget(TabWidget):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, api, parent=None):
        super().__init__(api, parent)

        self.active = False

        self.info_label = QLabel()
        self.info_label.setText("Positions")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        self.balances_label = QLabel()
        self.positions_list_widget = PositionsListWidget(self.api)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setAlignment(Qt.AlignCenter)
        self.scroll_area.setWidget(self.positions_list_widget)
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addWidget(self.scroll_area)

        self.setLayout(self.main_layout)

    def refresh(self):
        # rebuild positions list widget
        self.positions_list_widget.refresh()
        self.login_label.setText(self.get_login_label_text())

        self.repaint()
