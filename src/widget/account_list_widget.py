from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel

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
    def create_widgets(self):
         # re-create the widgets/ layout
        self.widgets = []
        self.group_box = QGroupBox()
        self.group_box.setTitle("Summary")
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)
        self.main_layout.addWidget(self.group_box)

    def __init__(self, api, parent=None):
        super().__init__(parent)

        # references to backend
        self.api = api

        # create main layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # will be done again in refresh
        self.create_widgets()

    def refresh(self):
        clear_layout(self.group_box_layout)
        clear_layout(self.main_layout)

        # re-create the widgets/ layouts
        self.create_widgets()

        accounts = self.api.get_accounts()
        account_list = get_account_list(accounts)

        if account_list: # create account widgets
            self.widgets = []
            for i, _ in enumerate(account_list):
                account = account_list[i]
                self.widgets.append(AccountWidget(i+1, account))
        else:
            self.widgets = [QLabel("No accounts available")]

        # add account widgets to groupbox layout
        for widget in self.widgets:
            self.group_box_layout.addWidget(widget)

        self.group_box_layout.addStretch()
        self.repaint()
