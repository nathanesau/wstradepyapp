from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel

from src.data import get_positions_list
from src.widget.positions_widget import PositionsWidget

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
        clear_layout(self.group_box_layout)

        positions = self.api.get_positions()
        positions_list = get_positions_list(positions)

        if positions_list: # create positions widget
            self.widgets = []
            for i, _ in enumerate(positions_list):
                positions = positions_list[i]
                self.widgets.append(PositionsWidget(i+1, positions))
        else: # create no positions available label
            self.widgets = [QLabel("No positions available")]

        # add positions widgets to groupbox layout
        for widget in self.widgets:
            self.group_box_layout.addWidget(widget)

        self.repaint()
