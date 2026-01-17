# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from .Standard import l_angle_standards , load_unequal_angles , load_equal_angles

from ...Qt.Core import Qt

from ...Qt.Widgets import (
    QDialog , QVBoxLayout , QHBoxLayout , QGroupBox , QLabel ,
    QComboBox , QTableWidget , QAbstractItemView , QMessageBox ,
    QDoubleSpinBox , QDialogButtonBox , QTableWidgetItem ,
    QCheckBox , QRadioButton
)


class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("L-Angle")
        self.setMinimumWidth(500)
        self.setMinimumHeight(450)
        self.current_standard = list(l_angle_standards.keys())[0]
        self.load_current_standard()
        self.setup_ui()

    def load_current_standard(self):
        folder, equal_csv, unequal_csv = l_angle_standards[self.current_standard]
        self.equal_angles = load_equal_angles(folder, equal_csv)
        self.unequal_angles = load_unequal_angles(folder, unequal_csv)

    def setup_ui(self):
        layout = QVBoxLayout(self)

        standard_group = QGroupBox("Standard")
        standard_layout = QHBoxLayout(standard_group)
        standard_layout.addWidget(QLabel("Select Standard:"))
        self.standard_combo = QComboBox()
        self.standard_combo.addItems(list(l_angle_standards.keys()))
        self.standard_combo.currentTextChanged.connect(self.on_standard_changed)
        standard_layout.addWidget(self.standard_combo)
        standard_layout.addStretch()
        layout.addWidget(standard_group)

        type_group = QGroupBox("Angle Type")
        type_layout = QHBoxLayout(type_group)

        self.equal_radio = QRadioButton("Equal Angle")
        self.unequal_radio = QRadioButton("Unequal Angle")
        self.equal_radio.setChecked(True)
        self.equal_radio.toggled.connect(self.on_type_changed)

        type_layout.addWidget(self.equal_radio)
        type_layout.addWidget(self.unequal_radio)

        self.mirror_check = QCheckBox("Mirror")
        type_layout.addWidget(self.mirror_check)

        type_layout.addStretch()

        layout.addWidget(type_group)

        size_group = QGroupBox("Select Size")
        size_layout = QVBoxLayout(size_group)

        self.size_table = QTableWidget()
        self.size_table.setColumnCount(8)
        self.size_table.setHorizontalHeaderLabels(["Shape", "Area (mm^2)", "Depth (mm)", "Width (mm)", "I_x (mm^4)", "I_y (mm^4)", "Plastic Modulus X (mm^3)", "Plastic Modulus Y (mm^3)"])
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

    def on_type_changed(self):
        self.populate_sizes()

    def get_current_sizes(self):
        if self.equal_radio.isChecked():
            return self.equal_angles
        return self.unequal_angles

    def populate_sizes(self):
        sizes = self.get_current_sizes()
        self.size_table.setRowCount(len(sizes))
        for row, size_data in enumerate(sizes):
            for col, value in enumerate(size_data):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.size_table.setItem(row, col, item)
        self.size_table.resizeColumnsToContents()
        if sizes:
            self.size_table.selectRow(0)

    def get_selected_size(self):
        row = self.size_table.currentRow()
        sizes = self.get_current_sizes()
        if row >= 0:
            return sizes[row]
        return None

    def get_angle_type(self):
        return "equal" if self.equal_radio.isChecked() else "unequal"

    def get_mirror(self):
        return self.mirror_check.isChecked()

    def get_length(self):
        return self.length_input.value()

    def accept(self):
        if self.get_selected_size() is None:
            QMessageBox.warning(self, "Warning", "Please select a size.")
            return
        super().accept()