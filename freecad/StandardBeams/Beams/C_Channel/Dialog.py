# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from .Standard import C_channel_standards , load_c_channel_sizes , load_c_channels

from ...Qt.Core import Qt

from ...Qt.Widgets import (
    QDialog , QVBoxLayout , QHBoxLayout , QGroupBox , QLabel ,
    QComboBox , QTableWidget , QAbstractItemView , QMessageBox ,
    QDoubleSpinBox , QDialogButtonBox , QTableWidgetItem
)


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("C-Channel")
        self.setMinimumWidth(550)
        self.setMinimumHeight(400)
        self.current_standard = list(C_channel_standards.keys())[0]

        self.load_current_standard()
        self.setup_ui()

    def load_current_standard(self):
        folder, channels_csv, sizes_csv = C_channel_standards[self.current_standard]
        self.c_channels = load_c_channels(folder, channels_csv)
        self.c_channel_sizes = load_c_channel_sizes(folder, sizes_csv)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        standard_group = QGroupBox("Standard")
        standard_layout = QHBoxLayout(standard_group)
        standard_layout.addWidget(QLabel("Select Standard:"))
        self.standard_combo = QComboBox()
        self.standard_combo.addItems(list(C_channel_standards.keys()))
        self.standard_combo.currentTextChanged.connect(self.on_standard_changed)
        standard_layout.addWidget(self.standard_combo)
        standard_layout.addStretch()
        layout.addWidget(standard_group)

        size_group = QGroupBox("Select Size")
        size_layout = QVBoxLayout(size_group)

        self.size_table = QTableWidget()
        self.size_table.setColumnCount(8)
        self.size_table.setHorizontalHeaderLabels([
            "Shape", "Area (mm^2)", "Depth (mm)", "Width (mm)", "I_x (mm^4)", "I_y (mm^4)", "Plastic Modulus X (mm^3)", "Plastic Modulus Y (mm^3)"
        ])
        self.size_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.size_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.size_table.horizontalHeader().setStretchLastSection(True)
        self.size_table.verticalHeader().setVisible(False)
        self.populate_sizes()
        size_layout.addWidget(self.size_table)

        layout.addWidget(size_group)

        length_group = QGroupBox("Beam Length")
        length_layout = QHBoxLayout(length_group)

        length_layout.addWidget(QLabel("Length:"))
        self.length_input = QDoubleSpinBox()
        self.length_input.setRange(1, 100000)
        self.length_input.setValue(1000)
        self.length_input.setSuffix(" mm")
        self.length_input.setDecimals(2)
        length_layout.addWidget(self.length_input)

        layout.addWidget(length_group)

        button_box = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def on_standard_changed(self, standard_name):
        self.current_standard = standard_name
        self.load_current_standard()
        self.populate_sizes()

    def populate_sizes(self):
        self.size_table.setRowCount(len(self.c_channels))
        for row, size_data in enumerate(self.c_channels):
            for col, value in enumerate(size_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.size_table.setItem(row, col, item)
        self.size_table.resizeColumnsToContents()
        if self.c_channels:
            self.size_table.selectRow(0)

    def get_selected_size(self):
        row = self.size_table.currentRow()
        if row >= 0:
            return self.c_channels[row]
        return None

    def get_length(self):
        return self.length_input.value()

    def accept(self):
        if self.get_selected_size() is None:
            QMessageBox.warning(self, "Warning", "Please select a size.")
            return
        super().accept()