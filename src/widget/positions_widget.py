from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel, QPushButton, \
    QGroupBox, QVBoxLayout, QGridLayout

from src.data import Position

class PositionsWidget(QWidget):
    # pylint: disable=too-many-instance-attributes
    def __init__(self, position_id, position: Position, parent=None):
        super().__init__(parent)
        self.position = position
        self.name_label = QLabel()
        self.symbol_label = QLabel()
        self.quantity_label = QLabel()
        self.price_label = QLabel()
        self.currency_label = QLabel()
        self.total_value_label = QLabel()

        if position.stock.get("name"):
            self.name_label.setText(position.stock.get("name"))
        if position.stock.get("symbol"):
            self.symbol_label.setText(position.stock.get("symbol"))
        if position.quantity:
            self.quantity_label.setText(str(position.quantity))
        if position.quote.get("amount"):
            self.price_label.setText(str(position.quote.get("amount")))
        if position.quote.get("currency"):
            self.currency_label.setText(position.quote.get("currency"))
        if position.quantity and position.quote.get("amount"):
            total_value = position.quantity * float(position.quote.get("amount"))
            self.total_value_label.setText('%.2f' % total_value)

        self.info_button = QPushButton()
        self.info_button.setText("Info")
        self.info_button.clicked.connect(self.on_info_button)

        self.group_box_layout = QGridLayout()
        self.group_box_layout.addWidget(QLabel("Name: "), 1, 1)
        self.group_box_layout.addWidget(self.name_label, 1, 2)
        self.group_box_layout.addWidget(QLabel("Symbol: "), 2, 1)
        self.group_box_layout.addWidget(self.symbol_label, 2, 2)
        self.group_box_layout.addWidget(QLabel("Quantity: "), 3, 1)
        self.group_box_layout.addWidget(self.quantity_label, 3, 2)
        self.group_box_layout.addWidget(QLabel("Price: "), 4, 1)
        self.group_box_layout.addWidget(self.price_label, 4, 2)
        self.group_box_layout.addWidget(QLabel("Currency: "), 5, 1)
        self.group_box_layout.addWidget(self.currency_label, 5, 2)
        self.group_box_layout.addWidget(QLabel("Total Value: "), 6, 1)
        self.group_box_layout.addWidget(self.total_value_label, 6, 2)
        self.group_box_layout.addWidget(self.infoButton, 7, 1, 1, 2)

        self.group_box = QGroupBox()
        self.group_box.setTitle("Position {}".format(position_id))
        self.group_box.setLayout(self.group_box_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.group_box)
        self.setLayout(self.main_layout)

    def on_info_button(self):
        msg = QMessageBox()
        msg.setText("Info message")
        msg.exec()
