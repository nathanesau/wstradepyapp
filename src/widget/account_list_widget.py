from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox

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
        clear_layout(self.group_box_layout)

        accounts = self.api.get_accounts()
        account_list = get_account_list(accounts)

        num_real_accounts = len(account_list)
        num_blank_accounts = max(0, 3 - num_real_accounts)

        # create account widgets
        self.widgets = []
        for i in range(num_real_accounts):
            account = account_list[i]
            widget = AccountWidget(i+1, account)
            self.widgets.append(widget)

        for i in range(num_real_accounts, num_real_accounts + num_blank_accounts):
            widget = AccountWidget(i+1)
            self.widgets.append(widget)

        # add account widgets to groupbox layout
        for widget in self.widgets:
            self.group_box_layout.addWidget(widget)

        self.repaint()
