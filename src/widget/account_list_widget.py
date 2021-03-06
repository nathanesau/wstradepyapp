from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QGroupBox

from src.data import get_account_list
from src.widget.account_widget import AccountWidget

# https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt/
def clear_layout(layout):
    for i in reversed(range(layout.count())):
        layout_item = layout.itemAt(i)
        if layout_item.widget() is not None:
            widget_to_remove = layout_item.widget()
            widget_to_remove.setParent(None)
            layout.removeWidget(widget_to_remove)
        elif layout_item.spacerItem() is not None:
            pass
        else:
            layout_to_remove = layout.itemAt(i)
            clear_layout(layout_to_remove)

# groupbox containing account widgets
class AccountListWidget(QWidget):
    def refresh_needed(self):
        pass

    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        # create list layout
        self.list_layout = QVBoxLayout()
        self.list_widget = QWidget()

        # create main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # cache
        self.last_refresh_email = None

        # widgets (created in refresh)
        self.widgets = []

    def refresh(self):
        if self.last_refresh_email == self.api.email:
            return

        self.last_refresh_email = self.api.email
        clear_layout(self.list_layout)
        clear_layout(self.main_layout)

        # re-create list layout
        self.list_layout = QVBoxLayout()
        self.list_widget = QWidget()

        # create self.widgets
        accounts = self.api.get_accounts()
        account_list = get_account_list(accounts)
        if account_list: # create account widgets
            self.widgets = []
            for i, _ in enumerate(account_list):
                account = account_list[i]
                self.widgets.append(AccountWidget(i+1, account))
        else:
            self.widgets = [QLabel("No accounts available")]

        # add self.widgets to layout
        for widget in self.widgets:
            self.list_layout.addWidget(widget)

        # add new widgets to main layout
        self.list_layout.addStretch()
        self.list_layout.setContentsMargins(0, 0, 0, 0)
        self.list_widget.setLayout(self.list_layout)
        self.main_layout.addWidget(self.list_widget)
        self.repaint()
