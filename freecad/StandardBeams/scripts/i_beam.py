# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.


import csv
import os
from PySide import QtWidgets, QtCore


I_beam_standards = {
    "European (EN 10365 IPE)": ("European", "EuropeanIPEBeams.csv", "EuropeanIPEBeamSizes.csv"),
    "European (EN 10365 IPN)": ("European", "EuropeanIPNBeams.csv", "EuropeanIPNBeamSizes.csv"),
}

def get_csv_path(folder, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, '..', 'Standards', folder, filename)

def load_i_beams(folder, filename):
    csv_path = get_csv_path(folder, filename)
    beams = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                beams.append(row)
    return beams


def load_i_beam_sizes(folder, filename):
    csv_path = get_csv_path(folder, filename)
    sizes = {}
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 5:
                name = row[0]
                sizes[name] = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
    return sizes


class IBeamDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("I-Beam")
        self.setMinimumWidth(550)
        self.setMinimumHeight(400)
        self.current_standard = list(I_beam_standards.keys())[0]
        
        self.load_current_standard()
        self.setup_ui()

    def load_current_standard(self):
        folder, beams_csv, sizes_csv = I_beam_standards[self.current_standard]
        self.I_beams = load_i_beams(folder, beams_csv)
        self.I_beam_sizes = load_i_beam_sizes(folder, sizes_csv)

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        standard_group = QtWidgets.QGroupBox("Standard")
        standard_layout = QtWidgets.QHBoxLayout(standard_group)
        standard_layout.addWidget(QtWidgets.QLabel("Select Standard:"))
        self.standard_combo = QtWidgets.QComboBox()
        self.standard_combo.addItems(list(I_beam_standards.keys()))
        self.standard_combo.currentTextChanged.connect(self.on_standard_changed)
        standard_layout.addWidget(self.standard_combo)
        standard_layout.addStretch()
        layout.addWidget(standard_group)

        size_group = QtWidgets.QGroupBox("Select Size")
        size_layout = QtWidgets.QVBoxLayout(size_group)

        self.size_table = QtWidgets.QTableWidget()
        self.size_table.setColumnCount(8)
        self.size_table.setHorizontalHeaderLabels([
            "Shape", "Area (mm^2)", "Depth (mm)", "Width (mm)", "I_x (mm^4)", "I_y (mm^4)", "Plastic Modulus X (mm^3)", "Plastic Modulus Y (mm^3)"
        ])
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
        self.size_table.setRowCount(len(self.I_beams))
        for row, size_data in enumerate(self.I_beams):
            for col, value in enumerate(size_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.size_table.setItem(row, col, item)
        self.size_table.resizeColumnsToContents()
        if self.I_beams:
            self.size_table.selectRow(0)

    def get_selected_size(self):
        row = self.size_table.currentRow()
        if row >= 0:
            return self.I_beams[row]
        return None

    def get_length(self):
        return self.length_input.value()

    def accept(self):
        if self.get_selected_size() is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a size.")
            return
        super().accept()


def create_i_beam(size_data, length, standard_name="European (EN 10365)"):
    
    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()
    
    folder, beams_csv, sizes_csv = I_beam_standards[standard_name]
    I_beam_sizes = load_i_beam_sizes(folder, sizes_csv)
    
    body = doc.addObject('PartDesign::Body', 'IBeamBody')

    name = f"IBeam_Sketch"
    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = I_beam_sizes.get(size_data[0])
    points = [
        [0, 0],
        [dimensions[1], 0],
        [dimensions[1], dimensions[2]],
        [(dimensions[1]/2) + (dimensions[3]/2), dimensions[2]],
        [(dimensions[1]/2) + (dimensions[3]/2), dimensions[0] - dimensions[2]],
        [dimensions[1], dimensions[0] - dimensions[2]],
        [dimensions[1], dimensions[0]],
        [0, dimensions[0]],
        [0, dimensions[0] - dimensions[2]],
        [(dimensions[1]/2) - (dimensions[3]/2), dimensions[0] - dimensions[2]],
        [(dimensions[1]/2) - (dimensions[3]/2), dimensions[2]],
        [0, dimensions[2]],
    ]

    for i, pt in enumerate(points):
        x1, y1 = pt
        x2, y2 = points[(i + 1) % len(points)]
        p1 = Vector(x1, y1, 0)
        p2 = Vector(x2, y2, 0)
        
        current_sketch.addGeometry(Part.LineSegment(p1, p2), False)

    pad = body.newObject('PartDesign::Pad', "IBeamPad")
    pad.Type = "Length" 
    pad.Profile = current_sketch
    pad.Length = length
    pad.Reversed = False
    pad.Midplane = False

    current_sketch.Visibility = False
    
    body.recompute()
    body.Tip = pad
    doc.recompute()
