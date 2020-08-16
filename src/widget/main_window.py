from PyQt5.QtWidgets import QMainWindow, QAction, QPushButton, QVBoxLayout, \
    QWidget, QTabWidget, QHBoxLayout
from PyQt5.QtGui import QIcon

from src import constants

from src.widget.about_dialog import AboutDialog
from src.widget.accounts_tab_widget import AccountsTabWidget
from src.widget.activity_tab_widget import ActivityTabWidget
from src.widget.funding_tab_widget import FundingTabWidget
from src.widget.login_dialog import LoginDialog
from src.widget.home_tab_widget import HomeTabWidget
from src.widget.positions_tab_widget import PositionsTabWidget
from src.widget.settings_tab_widget import SettingsTabWidget
from src.widget.ws_message_box import WSMessageBox

class MainWindow(QMainWindow):
    # pylint: disable=too-many-locals
    # pylint: disable=too-many-statements
    # pylint: disable=too-many-instance-attributes
    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        self.login_action = QAction("Login")
        self.login_action.triggered.connect(self.on_login)
        self.logout_action = QAction("Logout")
        self.logout_action.triggered.connect(self.on_logout)
        self.about_action = QAction("About")
        self.about_action.triggered.connect(self.on_about)

        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.login_action)
        file_menu.addAction(self.logout_action)
        help_menu = self.menuBar().addMenu("Help")
        help_menu.addAction(self.about_action)

        home_button = QPushButton('Home', self)
        positions_button = QPushButton('Positions', self)
        activity_button = QPushButton('Activity', self)
        funding_button = QPushButton('Funding', self)
        accounts_button = QPushButton('Accounts', self)
        settings_button = QPushButton('Settings', self)

        home_button.clicked.connect(self.on_home_button)
        positions_button.clicked.connect(self.on_positions_button)
        activity_button.clicked.connect(self.on_activity_button)
        funding_button.clicked.connect(self.on_funding_button)
        accounts_button.clicked.connect(self.on_accounts_button)
        settings_button.clicked.connect(self.on_settings_button)

        left_layout = QVBoxLayout()
        left_layout.addWidget(home_button)
        left_layout.addWidget(positions_button)
        left_layout.addWidget(activity_button)
        left_layout.addWidget(funding_button)
        left_layout.addWidget(accounts_button)
        left_layout.addWidget(settings_button)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)

        self.left_widget = QWidget()
        self.left_widget.setLayout(left_layout)
        self.home_widget = HomeTabWidget(api)
        self.positions_widget = PositionsTabWidget(api)
        self.activity_widget = ActivityTabWidget(api)
        self.funding_widget = FundingTabWidget(api)
        self.accounts_widget = AccountsTabWidget(api)
        self.settings_widget = SettingsTabWidget(api)
        self.right_widget = QTabWidget()
        self.right_widget.addTab(self.home_widget, '')
        self.right_widget.addTab(self.positions_widget, '')
        self.right_widget.addTab(self.activity_widget, '')
        self.right_widget.addTab(self.funding_widget, '')
        self.right_widget.addTab(self.accounts_widget, '')
        self.right_widget.addTab(self.settings_widget, '')
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; height: 0;}''')
        self.activate_home_tab()

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)
        self.setWindowTitle(constants.APP_NAME)
        self.setWindowIcon(QIcon(":icon.svg"))
        self.resize(600, 750)

    # refreshes data for active widget
    def refresh_active_widget(self):
        if self.home_widget.active:
            self.home_widget.refresh()
        elif self.positions_widget.active:
            self.positions_widget.refresh()
        elif self.activity_widget.active:
            self.activity_widget.refresh()
        elif self.funding_widget.active:
            self.funding_widget.refresh()
        elif self.accounts_widget.active:
            self.accounts_widget.refresh()
        elif self.settings_widget.active:
            self.settings_widget.refresh()

    def on_about(self):
        dlg = AboutDialog(self)
        dlg.exec()

    def on_login(self):
        dlg = LoginDialog(self.api, self)
        dlg.exec()

    def on_logout(self):
        self.api.clear_credentials()

        msg = WSMessageBox("Logged out successfully")
        msg.exec()

        self.refresh_active_widget()

    def activate_home_tab(self):
        self.right_widget.setCurrentIndex(0)
        self.home_widget.active = True
        self.positions_widget.active = False
        self.activity_widget.active = False
        self.funding_widget.active = False
        self.accounts_widget.active = False
        self.settings_widget.active = False

    def activate_positions_tab(self):
        self.right_widget.setCurrentIndex(1)
        self.home_widget.active = False
        self.positions_widget.active = True
        self.activity_widget.active = False
        self.funding_widget.active = False
        self.accounts_widget.active = False
        self.settings_widget.active = False

    def activate_activity_tab(self):
        self.right_widget.setCurrentIndex(2)
        self.home_widget.active = False
        self.positions_widget.active = False
        self.activity_widget.active = True
        self.funding_widget.active = False
        self.accounts_widget.active = False
        self.settings_widget.active = False

    def activate_funding_tab(self):
        self.right_widget.setCurrentIndex(3)
        self.home_widget.active = False
        self.positions_widget.active = False
        self.activity_widget.active = False
        self.funding_widget.active = True
        self.accounts_widget.active = False
        self.settings_widget.active = False

    def activate_accounts_tab(self):
        self.right_widget.setCurrentIndex(4)
        self.home_widget.active = False
        self.positions_widget.active = False
        self.activity_widget.active = False
        self.funding_widget.active = False
        self.accounts_widget.active = True
        self.settings_widget.active = False

    def activate_settings_tab(self):
        self.right_widget.setCurrentIndex(5)
        self.home_widget.active = False
        self.positions_widget.active = False
        self.activity_widget.active = False
        self.funding_widget.active = False
        self.accounts_widget.active = False
        self.settings_widget.active = True

    def on_home_button(self):
        self.activate_home_tab()
        self.refresh_active_widget()

    def on_positions_button(self):
        self.activate_positions_tab()
        self.refresh_active_widget()

    def on_activity_button(self):
        self.activate_activity_tab()
        self.refresh_active_widget()

    def on_funding_button(self):
        self.activate_funding_tab()
        self.refresh_active_widget()

    def on_accounts_button(self):
        self.activate_accounts_tab()
        self.refresh_active_widget()

    def on_settings_button(self):
        self.activate_settings_tab()
        self.refresh_active_widget()
