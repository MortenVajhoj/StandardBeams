# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.


import csv
import os
from PySide import QtWidgets, QtCore

from ..Misc.Imprint import imprint


square_tube_standards = {
    "European (EN 10210-2 SHS)": ("European", "EuropeanSquareTubes.csv"),
}


def get_csv_path(folder, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, '..', 'Standards', folder, filename)

def load_square_tubes(folder, filename):
    csv_path = get_csv_path(folder, filename)
    tubes = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                tubes.append(row)
    return tubes


class SquareTubeDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Square Tube")
        self.setMinimumWidth(400)
        self.current_standard = list(square_tube_standards.keys())[0]
        self.load_current_standard()
        self.setup_ui()

    def load_current_standard(self):
        folder, csv_file = square_tube_standards[self.current_standard]
        self.square_tubes = load_square_tubes(folder, csv_file)

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        standard_group = QtWidgets.QGroupBox("Standard")
        standard_layout = QtWidgets.QHBoxLayout(standard_group)
        standard_layout.addWidget(QtWidgets.QLabel("Select Standard:"))
        self.standard_combo = QtWidgets.QComboBox()
        self.standard_combo.addItems(list(square_tube_standards.keys()))
        self.standard_combo.currentTextChanged.connect(self.on_standard_changed)
        standard_layout.addWidget(self.standard_combo)
        standard_layout.addStretch()
        layout.addWidget(standard_group)

        size_group = QtWidgets.QGroupBox("Select Size")
        size_layout = QtWidgets.QVBoxLayout(size_group)

        self.size_table = QtWidgets.QTableWidget()
        self.size_table.setColumnCount(8)
        self.size_table.setHorizontalHeaderLabels(["Shape", "Area (mm^2)", "Depth (mm)", "Width (mm)", "I_x (mm^4)", "I_y (mm^4)", "Plastic Modulus X (mm^3)", "Plastic Modulus Y (mm^3)"])
        self.size_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.size_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.size_table.horizontalHeader().setStretchLastSection(True)
        self.size_table.verticalHeader().setVisible(False)
        self.populate_sizes()
        size_layout.addWidget(self.size_table)

        layout.addWidget(size_group)

        length_group = QtWidgets.QGroupBox("Beam Length")
        length_layout = QtWidgets.QHBoxLayout(length_group)

        length_layout.addWidget(QtWidgets.QLabel("Length:"))
        self.length_input = QtWidgets.QDoubleSpinBox()
        self.length_input.setRange(1, 100000)
        self.length_input.setValue(1000)
        self.length_input.setSuffix(" mm")
        self.length_input.setDecimals(2)
        length_layout.addWidget(self.length_input)

        layout.addWidget(length_group)

        button_box = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def on_standard_changed(self, standard_name):
        self.current_standard = standard_name
        self.load_current_standard()
        self.populate_sizes()

    def populate_sizes(self):
        self.size_table.setRowCount(len(self.square_tubes))
        for row, size_data in enumerate(self.square_tubes):
            for col, value in enumerate(size_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.size_table.setItem(row, col, item)
        self.size_table.resizeColumnsToContents()
        if self.square_tubes:
            self.size_table.selectRow(0)

    def get_selected_size(self):
        row = self.size_table.currentRow()
        if row >= 0:
            return self.square_tubes[row]
        return None

    def get_length(self):
        return self.length_input.value()

    def accept(self):
        if self.get_selected_size() is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a size.")
            return
        super().accept()


def create_square_tube(size_data, length):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()
    
    body = doc.addObject('PartDesign::Body', 'SquareTubeBody')

    imprint(body)

    name = f"SquareTube_Sketch"

    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = size_data[0].split('x')
    outer_points = [
        [0, 0],
        [0, float(dimensions[0])],
        [float(dimensions[1]), float(dimensions[0])],
        [float(dimensions[1]), 0],
    ]

    inner_points = [
        [float(dimensions[2]), float(dimensions[2])],
        [float(dimensions[2]), float(dimensions[0]) - float(dimensions[2])],
        [float(dimensions[1]) - float(dimensions[2]), float(dimensions[0]) - float(dimensions[2])],
        [float(dimensions[1]) - float(dimensions[2]), float(dimensions[2])],
    ]

    for i, pt in enumerate(outer_points):
        x1, y1 = pt
        x2, y2 = outer_points[(i + 1) % len(outer_points)]
        p1 = Vector(x1, y1, 0)
        p2 = Vector(x2, y2, 0)
        
        current_sketch.addGeometry(Part.LineSegment(p1, p2), False)

    for i, pt in enumerate(inner_points):
        x1, y1 = pt
        x2, y2 = inner_points[(i + 1) % len(inner_points)]
        p1 = Vector(x1, y1, 0)
        p2 = Vector(x2, y2, 0)
        
        current_sketch.addGeometry(Part.LineSegment(p1, p2), False)

    pad = body.newObject('PartDesign::Pad', "TubePad")
    pad.Type = "Length" 
    pad.Profile = current_sketch
    pad.Length = length
    pad.Reversed = False
    pad.Midplane = False

    current_sketch.Visibility = False

    body.recompute()
    body.Tip = pad
    doc.recompute()
