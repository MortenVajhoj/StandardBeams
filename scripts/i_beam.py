

from PySide import QtWidgets, QtCore, QtGui

I_beams = [
["IPE 80", "764", "80", "46", "801000", "84900", "23200", "5820"],
["IPE 100", "1032", "100", "55", "1710000", "159000", "39400", "9150"],
["IPE 120", "1321", "120", "64", "3180000", "277000", "60700", "13600"],
["IPE 140", "1643", "140", "73", "5410000", "449000", "88300", "19300"],
["IPE 160", "2009", "160", "82", "8690000", "683000", "124000", "26100"],
["IPE 180", "2395", "180", "91", "13200000", "1010000", "166000", "34600"],
["IPE 200", "2848", "200", "100", "19400000", "1420000", "221000", "44600"],
["IPE 220", "3337", "220", "110", "27700000", "2050000", "285000", "58100"],
["IPE 240", "3912", "240", "120", "38900000", "2840000", "367000", "73900"],
["IPE 270", "4594", "270", "135", "57900000", "4200000", "484000", "97000"],
["IPE 300", "5381", "300", "150", "83600000", "6040000", "628000", "125000"],
["IPE 330", "6261", "330", "160", "118000000", "7880000", "804000", "154000"],
["IPE 360", "7273", "360", "170", "163000000", "10400000", "1020000", "191000"],
["IPE 400", "8446", "400", "180", "231000000", "13200000", "1310000", "229000"],
["IPE 450", "9882", "450", "190", "337000000", "16800000", "1700000", "276000"],
["IPE 500", "11550", "500", "200", "482000000", "21400000", "2190000", "336000"],
["IPE 550", "13440", "550", "210", "671000000", "26700000", "2790000", "401000"],
["IPE 600", "15600", "600", "220", "921000000", "33900000", "3510000", "486000"],
["IPE 750x137", "17460", "753", "263", "1600000000", "51700000", "4870000", "614000"],
["IPE 750x147", "18750", "753", "265", "1660000000", "52900000", "5110000", "631000"],
["IPE 750x173", "22130", "762", "267", "2060000000", "68700000", "6220000", "810000"],
["IPE 750x196", "25080", "770", "268", "2400000000", "81800000", "7170000", "959000"],
["IPE A 80", "638", "78", "46", "644000", "68500", "19000", "4690"],
["IPE A 100", "878", "98", "55", "1410000", "131000", "33000", "7540"],
["IPE A 120", "1103", "117.6", "64", "2570000", "224000", "49900", "11000"],
["IPE A 140", "1339", "137.4", "73", "4350000", "364000", "71600", "15500"],
["IPE A 160", "1618", "157", "82", "6890000", "544000", "99100", "20700"],
["IPE A 180", "1958", "177", "91", "10600000", "819000", "135000", "28000"],
["IPE A 200", "2347", "197", "100", "15900000", "1170000", "182000", "36500"],
["IPE A 220", "2826", "217", "110", "23200000", "1710000", "240000", "48500"],
["IPE A 240", "3331", "237", "120", "32900000", "2400000", "312000", "62400"],
["IPE A 270", "3915", "267", "135", "49200000", "3580000", "413000", "82300"],
["IPE A 300", "4653", "297", "150", "71700000", "5190000", "542000", "107000"],
["IPE A 330", "5474", "327", "160", "102000000", "6850000", "702000", "133000"],
["IPE A 360", "6396", "357.6", "170", "145000000", "9440000", "907000", "172000"],
["IPE A 400", "7310", "397", "180", "203000000", "11700000", "1140000", "202000"],
["IPE A 450", "8555", "447", "190", "298000000", "15000000", "1490000", "246000"],
["IPE A 500", "10110", "497", "200", "429000000", "19400000", "1950000", "302000"],
["IPE A 550", "11730", "547", "210", "600000000", "24300000", "2480000", "362000"],
["IPE A 600", "13700", "597", "220", "829000000", "31200000", "3140000", "442000"],
["IPE O 180", "2710", "182", "92", "15100000", "1170000", "189000", "39900"],
["IPE O 200", "3196", "202", "102", "22100000", "1690000", "249000", "51900"],
["IPE O 220", "3739", "222", "112", "31300000", "2400000", "321000", "66900"],
["IPE O 240", "4371", "242", "122", "43700000", "3290000", "410000", "84400"],
["IPE O 270", "5384", "274", "136", "69500000", "5140000", "575000", "118000"],
["IPE O 300", "6283", "304", "152", "99900000", "7460000", "744000", "153000"],
["IPE O 330", "7262", "334", "162", "139000000", "9600000", "943000", "185000"],
["IPE O 360", "8413", "364", "172", "191000000", "12500000", "1190000", "227000"],
["IPE O 400", "9639", "404", "182", "268000000", "15600000", "1500000", "269000"],
["IPE O 450", "11770", "456", "192", "409000000", "20900000", "2050000", "341000"],
["IPE O 500", "13670", "506", "202", "578000000", "26200000", "2610000", "409000"],
["IPE O 550", "15610", "556", "212", "792000000", "32200000", "3260000", "481000"],
["IPE O 600", "19680", "610", "224", "1180000000", "45200000", "4470000", "640000"],
]

I_beam_sizes = {
    "IPE 80": [80, 46, 5.2, 3.8],
    "IPE 100": [100, 55, 5.7, 4.1],
    "IPE 120": [120, 64, 6.3, 4.4],
    "IPE 140": [140, 73, 6.9, 4.7],
    "IPE 160": [160, 82, 7.4, 5.0],
    "IPE 180": [180, 91, 8.0, 5.3],
    "IPE 200": [200, 100, 8.5, 5.6],
    "IPE 220": [220, 110, 9.2, 5.9],
    "IPE 240": [240, 120, 9.8, 6.2],
    "IPE 270": [270, 135, 10.2, 6.6],
    "IPE 300": [300, 150, 10.7, 7.1],
    "IPE 330": [330, 160, 11.5, 7.5],
    "IPE 360": [360, 170, 12.7, 8.0],
    "IPE 400": [400, 180, 13.5, 8.6],
    "IPE 450": [450, 190, 14.6, 9.4],
    "IPE 500": [500, 200, 16.0, 10.2],
    "IPE 550": [550, 210, 17.2, 11.1],
    "IPE 600": [600, 220, 19.0, 12.0],
    "IPE 750x137": [753, 263, 17.0, 11.5],
    "IPE 750x147": [753, 265, 17.0, 13.2],
    "IPE 750x173": [762, 267, 21.6, 14.4],
    "IPE 750x196": [770, 268, 25.4, 15.6],
    "IPE A 80": [78, 46, 4.2, 3.3],
    "IPE A 100": [98, 55, 4.7, 3.6],
    "IPE A 120": [117.6, 64, 5.1, 3.8],
    "IPE A 140": [137.4, 73, 5.6, 3.8],
    "IPE A 160": [157, 82, 5.9, 4.0],
    "IPE A 180": [177, 91, 6.5, 4.3],
    "IPE A 200": [197, 100, 7.0, 4.5],
    "IPE A 220": [217, 110, 7.7, 5.0],
    "IPE A 240": [237, 120, 8.3, 5.2],
    "IPE A 270": [267, 135, 8.7, 5.5],
    "IPE A 300": [297, 150, 9.2, 6.1],
    "IPE A 330": [327, 160, 10.0, 6.5],
    "IPE A 360": [357.6, 170, 11.5, 6.6],
    "IPE A 400": [397, 180, 12.0, 7.0],
    "IPE A 450": [447, 190, 13.1, 7.6],
    "IPE A 500": [497, 200, 14.5, 8.4],
    "IPE A 550": [547, 210, 15.7, 9.0],
    "IPE A 600": [597, 220, 17.5, 9.8],
    "IPE O 180": [182, 92, 9.0, 6.0],
    "IPE O 200": [202, 102, 9.5, 6.2],
    "IPE O 220": [222, 112, 10.2, 6.6],
    "IPE O 240": [242, 122, 10.8, 7.0],
    "IPE O 270": [274, 136, 12.2, 7.5],
    "IPE O 300": [304, 152, 12.7, 8.0],
    "IPE O 330": [334, 162, 13.5, 8.5],
    "IPE O 360": [364, 172, 14.7, 9.2],
    "IPE O 400": [404, 182, 15.5, 9.7],
    "IPE O 450": [456, 192, 17.6, 11.0],
    "IPE O 500": [506, 202, 19.0, 12.0],
    "IPE O 550": [556, 212, 20.2, 12.7],
    "IPE O 600": [610, 224, 24.0, 15.0],
}


class IBeamDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("I-Beam")
        self.setMinimumWidth(550)
        self.setMinimumHeight(400)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

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

    def populate_sizes(self):
        self.size_table.setRowCount(len(I_beams))
        for row, size_data in enumerate(I_beams):
            for col, value in enumerate(size_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.size_table.setItem(row, col, item)
        self.size_table.resizeColumnsToContents()
        if I_beams:
            self.size_table.selectRow(0)

    def get_selected_size(self):
        row = self.size_table.currentRow()
        if row >= 0:
            return I_beams[row]
        return None

    def get_length(self):
        return self.length_input.value()

    def accept(self):
        if self.get_selected_size() is None:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a size.")
            return
        super().accept()


def create_i_beam(size_data, length):
    
    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()
    
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
