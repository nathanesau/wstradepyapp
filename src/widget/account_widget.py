from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QGroupBox, \
    QVBoxLayout

class AccountWidget(QWidget):
    def create_dynamic_widgets(self, rows):
        row_num = 0
        for row_text, row_widget in rows.items():
            row_num += 1
            self.group_box_layout.addWidget(QLabel(row_text), row_num, 1)
            self.group_box_layout.addWidget(row_widget, row_num, 2)

        self.group_box.setLayout(self.group_box_layout)
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

    def __init__(self, account_id, account=None, parent=None):
        super().__init__(parent)
        self.created_label = QLabel('N/A')
        self.balance_label = QLabel('N/A')
        self.deposits_label = QLabel('N/A')
        self.type_label = QLabel('N/A')
        self.group_box_layout = QGridLayout()
        self.group_box = QGroupBox()
        self.main_layout = QVBoxLayout()

        # permanent widgets
        self.group_box.setTitle("Account {}".format(account_id))

        if account and account.created_at:
            self.created_label.setText(str(account.created_at))
        if account and account.current_balance:
            self.balance_label.setText(str(account.current_balance))
        if account and account.net_deposits:
            self.deposits_label.setText(str(account.net_deposits))
        if account and account.account_type:
            self.type_label.setText(str(account.account_type))

        self.create_dynamic_widgets({"Created: ": self.created_label,
                                     "Balance: ": self.balance_label,
                                     "Deposits: ": self.deposits_label,
                                     "Type: ": self.type_label})
