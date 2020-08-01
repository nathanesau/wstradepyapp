# part of wstradepyapp - frontend

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from typing import List

from src import api
from src import constants
from src.data import *

# https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt/
def clearLayout(layout):
    #print("-- -- input layout: "+str(layout))
    for i in reversed(range(layout.count())):
        layoutItem = layout.itemAt(i)
        if layoutItem.widget() is not None:
            widgetToRemove = layoutItem.widget()
            #print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            layout.removeWidget(widgetToRemove)
        elif layoutItem.spacerItem() is not None:
            pass
            #print("found spacer: " + str(layoutItem.spacerItem()))
        else:
            layoutToRemove = layout.itemAt(i)
            #$print("-- found Layout: "+str(layoutToRemove))
            clearLayout(layoutToRemove)

class WSMessageBox(QMessageBox):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setWindowIcon(QIcon(":icon.svg"))
        self.setWindowTitle("Info")

class MainWindow(QMainWindow):
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
        self.resize(500, 500)

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

class AccountWidget(QWidget):
    def __init__(self, account_id, account: Account, parent=None):
        super().__init__(parent)
        self.created_label =  QLabel()
        self.balance_label = QLabel()
        self.deposits_label = QLabel()
        self.type_label = QLabel()

        if account.created_at:
            self.created_label.setText(str(account.created_at))
        if account.current_balance:
            self.balance_label.setText(str(account.current_balance))
        if account.net_deposits:
            self.deposits_label.setText(str(account.net_deposits))
        if account.account_type:
            self.type_label.setText(str(account.account_type))

        self.group_box_layout = QGridLayout()
        self.group_box_layout.addWidget(QLabel("Created: "), 1, 1)
        self.group_box_layout.addWidget(self.created_label, 1, 2)
        self.group_box_layout.addWidget(QLabel("Balance: "), 2, 1)
        self.group_box_layout.addWidget(self.balance_label, 2, 2)
        self.group_box_layout.addWidget(QLabel("Deposits: "), 3, 1)
        self.group_box_layout.addWidget(self.deposits_label, 3, 2)
        self.group_box_layout.addWidget(QLabel("Type: "), 4, 1)
        self.group_box_layout.addWidget(self.type_label, 4, 2)

        self.group_box = QGroupBox()
        self.group_box.setTitle("Account {}".format(account_id))
        self.group_box.setLayout(self.group_box_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

# groupbox containing account widgets
class AccountListWidget(QWidget):
    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        # refreshed in "refresh"
        # widgets get added to groupbox layout
        self.widgets = []

        self.group_box_layout = QVBoxLayout()
        self.group_box = QGroupBox()
        self.group_box.setTitle("Summary")
        self.group_box.setLayout(self.group_box_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

    def refresh(self):
        clearLayout(self.group_box_layout)

        accounts = self.api.get_accounts()
        account_list = get_account_list(accounts)

        if account_list: # create account widgets
            self.widgets = []
            for i in range(len(account_list)):
                account = account_list[i]
                self.widgets.append(AccountWidget(i+1, account))
        else: # create no account available label
            self.widgets = [QLabel("No accounts available")]

        # add account widgets to groupbox layout
        for widget in self.widgets:
            self.group_box_layout.addWidget(widget)

        self.repaint()

class PositionsWidget(QWidget):
    def __init__(self, position_id, position: Position, parent=None):
        super().__init__(parent)
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()

        self.label1.setText("Text 1")
        self.label2.setText("Text 2")
        self.label3.setText("Text 3")

        self.group_box_layout = QGridLayout()
        self.group_box_layout.addWidget(QLabel("Label1: "), 1, 1)
        self.group_box_layout.addWidget(self.label1, 1, 2)
        self.group_box_layout.addWidget(QLabel("Label2: "), 2, 1)
        self.group_box_layout.addWidget(self.label2, 2, 2)
        self.group_box_layout.addWidget(QLabel("Label3: "), 3, 1)
        self.group_box_layout.addWidget(self.label3, 3, 2)

        self.group_box = QGroupBox()
        self.group_box.setTitle("Position{}".format(position_id))
        self.group_box.setLayout(self.group_box_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

# groupbox containing positions widgets
class PositionsListWidget(QWidget):
    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        # refreshed in "refresh"
        # widgets get added to groupbox layout
        self.widgets = []
        
        self.group_box_layout = QVBoxLayout()
        self.group_box = QGroupBox()
        self.group_box.setTitle("Positions")
        self.group_box.setLayout(self.group_box_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

    def refresh(self):
        clearLayout(self.group_box_layout)
        
        positions = self.api.get_positions()
        positions_list = get_positions_list(positions)

        if positions_list: # create positions widget
            self.widgets = []
            for i in range(len(positions_list)):
                positions = positions_list[i]
                self.widgets.append(PositionsWidget(i+1, positions))
        else: # create no positions available label
            self.widgets = [QLabel("No positions available")]

        # add positions widgets to groupbox layout
        for widget in self.widgets:
            self.group_box_layout.addWidget(widget)

        self.repaint()

class HomeTabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}.".format(self.api.get_login_name())
        elif self.api.has_access_token():
            return "Access token has expired. Please login again."
        else:
            return "User has not logged in."

    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.active = False

        # references to backend
        self.api = api

        self.info_label = QLabel()
        self.info_label.setText("Home")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        self.balances_label = QLabel()
        self.account_list_widget = AccountListWidget(self.api)
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addWidget(self.account_list_widget)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        # rebuild account list widget
        self.account_list_widget.refresh()
        self.login_label.setText(self.get_login_label_text())

        self.repaint()

class PositionsTabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}".format(self.api.get_login_name())
        elif self.api.has_access_token():
            return "Access token has expired. Please login again."
        else:
            return "User has not logged in"

    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.active = False

        # references to backend
        self.api = api
        
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
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addWidget(self.positions_list_widget)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        # rebuild positions list widget
        self.positions_list_widget.refresh()
        self.login_label.setText(self.get_login_label_text())

        self.repaint()

class ActivityTabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}.".format(self.api.get_login_name())
        elif self.api.has_access_token():
            return "Access token has expired. Please login again."
        else:
            return "User has not logged in."

    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.active = False

        # references to backend
        self.api = api

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
        # TODO: add other labels here
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        # TODO: refresh other labels here
        self.login_label.setText(self.get_login_label_text())
        self.repaint()

class FundingTabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}.".format(self.api.get_login_name())
        elif self.api.has_access_token():
            return "Access token has expired. Please login again."
        else:
            return "User has not logged in."

    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.active = False

        # references to backend
        self.api = api

        self.info_label = QLabel()
        self.info_label.setText("Funding")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        # TODO: add other labels here
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        # TODO: refresh other labels here
        self.login_label.setText(self.get_login_label_text())

class AccountsTabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}.".format(self.api.get_login_name())
        elif self.api.has_access_token():
            return "Access token has expired. Please login again."
        else:
            return "User has not logged in."

    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.active = False

        # references to backend
        self.api = api

        self.info_label = QLabel()
        self.info_label.setText("Accounts")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")
        
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        # TODO: add other labels here
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        # TODO: refresh other labels here
        self.login_label.setText(self.get_login_label_text())

class SettingsTabWidget(QWidget):
    def get_login_label_text(self):
        if self.api.is_authenticated():
            return "Logged in as: {}.".format(self.api.get_login_name())
        elif self.api.has_access_token():
            return "Access token has expired. Please login again."
        else:
            return "User has not logged in."

    def __init__(self, api, parent=None):
        super().__init__(parent)
        self.active = False

        # references to backend
        self.api = api

        self.info_label = QLabel()
        self.info_label.setText("Settings")
        self.info_label.setStyleSheet("font-size: 12pt; font-weight: bold")

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh)
        self.title_layout = QHBoxLayout()
        self.title_layout.addWidget(self.info_label)
        self.title_layout.addStretch(1)
        self.title_layout.addWidget(self.refresh_button)

        self.login_label = QLabel()
        # TODO: add other labels here
        self.refresh()

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.title_layout)
        self.main_layout.addWidget(self.login_label)
        self.main_layout.addStretch(5)

        self.setLayout(self.main_layout)

    def refresh(self):
        # TODO: refresh other labels here
        self.login_label.setText(self.get_login_label_text())

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

class LoginDialog(QDialog):
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
        credentials = { "email": email, "password": password }
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