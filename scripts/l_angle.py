
from PySide import QtWidgets, QtCore, QtGui

equal_angles = [
    ["20x20x3", "112", "20", "20", "6100", "1600", "743", "371.5"],
    ["25x25x3", "142", "25", "25", "12600", "3300", "1188", "594"],
    ["25x25x4", "185", "25", "25", "16000", "4300", "1530", "765"],
    ["30x30x3", "174", "30", "30", "22300", "5800", "1746", "873"],
    ["30x30x4", "227", "30", "30", "28600", "7500", "2258", "1129"],
    ["35x35x4", "267", "35", "35", "46900", "12200", "3122", "1561"],
    ["40x40x4", "308", "40", "40", "71000", "18400", "4133", "2066.5"],
    ["40x40x5", "379", "40", "40", "86100", "22500", "5051", "2525.5"],
    ["45x45x4.5", "390", "45", "45", "113500", "29400", "5887", "2943.5"],
    ["50x50x4", "389", "50", "50", "142500", "36900", "6574", "3287"],
    ["50x50x5", "480", "50", "50", "174200", "45100", "8066", "4033"],
    ["50x50x6", "569", "50", "50", "203700", "53100", "9506", "4753"],
    ["60x60x5", "582", "60", "60", "307800", "79700", "11791", "5895.5"],
    ["60x60x6", "691", "60", "60", "362100", "93800", "13932", "6966"],
    ["60x60x8", "903", "60", "60", "462000", "121100", "18032", "9016"],
    ["65x65x7", "870", "65", "65", "530900", "137800", "18949", "9474.5"],
    ["70x70x6", "813", "70", "70", "586100", "151600", "19209", "9604.5"],
    ["70x70x7", "940", "70", "70", "671900", "174000", "22117", "11059"],
    ["75x75x6", "873", "75", "75", "724000", "187400", "22177", "11089"],
    ["75x75x8", "1140", "75", "75", "934900", "242500", "28849", "14425"],
    ["80x80x8", "1230", "80", "80", "1148000", "297200", "33007", "16504"],
    ["80x80x10", "1510", "80", "80", "1388000", "362300", "40348", "20174"],
    ["90x90x7", "1220", "90", "90", "1471000", "380200", "37308", "18654"],
    ["90x90x8", "1390", "90", "90", "1659000", "428700", "42197", "21099"],
    ["90x90x9", "1550", "90", "90", "1840000", "476300", "46990", "23495"],
    ["90x90x10", "1710", "90", "90", "2015000", "523200", "51690", "25845"],
    ["100x100x8", "1550", "100", "100", "2302000", "594700", "52522", "26261"],
    ["100x100x10", "1920", "100", "100", "2807000", "726500", "64450", "32225"],
    ["100x100x12", "2270", "100", "100", "3280000", "854200", "75967", "37984"],
    ["110x110x10", "2120", "110", "110", "3782000", "977200", "78629", "39315"],
    ["110x110x12", "2510", "110", "110", "4433000", "1150000", "92809", "46405"],
    ["120x120x10", "2320", "120", "120", "4976000", "1283000", "94186", "47093"],
    ["120x120x11", "2540", "120", "120", "5415000", "1398000", "102810", "51406"],
    ["120x120x12", "2750", "120", "120", "5843000", "1510000", "111310", "55655"],
    ["120x120x13", "2970", "120", "120", "6259000", "1622000", "119690", "59843"],
    ["120x120x15", "3390", "120", "120", "7056000", "1842000", "136080", "68039"],
    ["130x130x12", "3000", "130", "130", "7506000", "1937000", "131550", "65775"],
    ["140x140x10", "2724", "140", "140", "8020000", "2070000", "129630", "64814"],
    ["140x140x13", "3495", "140", "140", "10200000", "2620000", "165190", "82596"],
    ["150x150x10", "2930", "150", "150", "9920000", "2560000", "149480", "74740"],
    ["150x150x12", "3480", "150", "150", "11720000", "3020000", "177130", "88567"],
    ["150x150x14", "4030", "150", "150", "13440000", "3469000", "204130", "102060"],
    ["150x150x15", "4300", "150", "150", "14270000", "3689000", "217390", "108690"],
    ["150x150x18", "5100", "150", "150", "16660000", "4338000", "256250", "128130"],
    ["160x160x14", "4320", "160", "160", "16440000", "4238000", "233490", "116750"],
    ["160x160x15", "4610", "160", "160", "17470000", "4508000", "248740", "124370"],
    ["160x160x16", "4900", "160", "160", "18480000", "4776000", "263830", "131910"],
    ["160x160x17", "5180", "160", "160", "19470000", "5041000", "278740", "139370"],
    ["180x180x13", "4550", "180", "180", "22210000", "5716000", "278260", "139130"],
    ["180x180x14", "4880", "180", "180", "23750000", "6113000", "298110", "149060"],
    ["180x180x15", "5210", "180", "180", "25270000", "6505000", "317760", "158880"],
    ["180x180x16", "5540", "180", "180", "26750000", "6894000", "337210", "168610"],
    ["180x180x17", "5870", "180", "180", "28220000", "7278000", "356480", "178240"],
    ["180x180x18", "6190", "180", "180", "29650000", "7660000", "375550", "187770"],
    ["180x180x19", "6510", "180", "180", "31060000", "8038000", "394440", "197220"],
    ["180x180x20", "6840", "180", "180", "32440000", "8413000", "413140", "206570"],
    ["200x200x15", "5810", "200", "200", "35160000", "9030000", "395190", "197600"],
    ["200x200x16", "6180", "200", "200", "37260000", "9570000", "419580", "209790"],
    ["200x200x17", "6550", "200", "200", "39320000", "10110000", "443760", "221880"],
    ["200x200x18", "6910", "200", "200", "41350000", "10640000", "467710", "233860"],
    ["200x200x19", "7270", "200", "200", "43350000", "11170000", "491450", "245730"],
    ["200x200x20", "7630", "200", "200", "45320000", "11690000", "514980", "257490"],
    ["200x200x21", "7990", "200", "200", "47250000", "12210000", "538310", "269160"],
    ["200x200x22", "8350", "200", "200", "49150000", "12730000", "561440", "280720"],
    ["200x200x23", "8710", "200", "200", "51020000", "13240000", "584360", "292180"],
    ["200x200x24", "9100", "200", "200", "52860000", "13750000", "607090", "303540"],
    ["200x200x25", "9410", "200", "200", "54670000", "14260000", "629630", "314810"],
    ["200x200x26", "9760", "200", "200", "56450000", "14760000", "651970", "325990"],
    ["203x203x19", "7360", "203", "203", "45880000", "11740000", "506500", "253250"],
    ["203x203x22.2", "8500", "203", "203", "52360000", "13500000", "583520", "291760"],
    ["203x203x25.4", "9680", "203", "203", "58500000", "15220000", "658460", "329230"],
    ["203x203x28.6", "10800", "203", "203", "64320000", "16920000", "731420", "365710"],
    ["250x250x20", "9640", "250", "250", "91440000", "23410000", "819080", "409540"],
    ["250x250x21", "10100", "250", "250", "95480000", "24470000", "856870", "428440"],
    ["250x250x22", "10600", "250", "250", "99460000", "25510000", "894400", "447200"],
    ["250x250x23", "11000", "250", "250", "103400000", "26550000", "931660", "465830"],
    ["250x250x24", "11500", "250", "250", "107300000", "27590000", "968650", "484330"],
    ["250x250x25", "11900", "250", "250", "111100000", "28610000", "1005400", "502690"],
    ["250x250x26", "12400", "250", "250", "114900000", "29630000", "1041900", "520930"],
    ["250x250x27", "12800", "250", "250", "118600000", "30650000", "1078100", "539040"],
    ["250x250x28", "13300", "250", "250", "122300000", "31660000", "1114100", "557030"],
    ["250x250x35", "16300", "250", "250", "146700000", "38590000", "1359100", "679540"],
]

unequal_angles = [
    ["120x80x8", "1549", "120", "80", "2600000", "463900", "55862", "22270"],
    ["120x80x10", "1913", "120", "80", "3170000", "566000", "68376", "27544"],
    ["120x80x12", "2269", "120", "80", "3707000", "664600", "80384", "32371"],
    ["130x65x8", "1509", "130", "65", "2786000", "287200", "57754", "16058"],
    ["130x65x10", "1863", "130", "65", "3396000", "350200", "70659", "20002"],
    ["150x75x9", "1960", "150", "75", "4832000", "499500", "86584", "24038"],
    ["150x75x10", "2170", "150", "75", "5311000", "548700", "95308", "26665"],
    ["150x75x11", "2370", "150", "75", "5779000", "597000", "103880", "29289"],
    ["150x75x12", "2570", "150", "75", "6235000", "644500", "112310", "31911"],
    ["150x90x10", "2320", "150", "90", "5913000", "879300", "103250", "36465"],
    ["150x90x11", "2530", "150", "90", "6437000", "957100", "112600", "39971"],
    ["150x100x10", "2420", "150", "100", "6373000", "1138000", "108940", "43441"],
    ["150x100x12", "2870", "150", "100", "7493000", "1339000", "128580", "51691"],
    ["150x100x14", "3320", "150", "100", "8559000", "1534000", "147590", "59830"],
    ["160x80x10", "2318", "160", "80", "6487000", "670100", "109110", "30377"],
    ["160x80x12", "2754", "160", "80", "7628000", "787700", "128690", "36350"],
    ["200x100x10", "2920", "200", "100", "12940000", "1345000", "173270", "47572"],
    ["200x100x12", "3480", "200", "100", "15290000", "1585000", "204970", "56925"],
    ["200x100x14", "4030", "200", "100", "17550000", "1817000", "235800", "66257"],
]


class LAngleDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("L-Angle")
        self.setMinimumWidth(500)
        self.setMinimumHeight(450)
        self.setup_ui()

    def setup_ui(self):
        layout = QtWidgets.QVBoxLayout(self)

        type_group = QtWidgets.QGroupBox("Angle Type")
        type_layout = QtWidgets.QHBoxLayout(type_group)

        self.equal_radio = QtWidgets.QRadioButton("Equal Angle")
        self.unequal_radio = QtWidgets.QRadioButton("Unequal Angle")
        self.equal_radio.setChecked(True)
        self.equal_radio.toggled.connect(self.on_type_changed)

        type_layout.addWidget(self.equal_radio)
        type_layout.addWidget(self.unequal_radio)
        
        self.mirror_check = QtWidgets.QCheckBox("Mirror")
        type_layout.addWidget(self.mirror_check)
        
        type_layout.addStretch()

        layout.addWidget(type_group)

        size_group = QtWidgets.QGroupBox("Select Size- From EN1993-1-1:2005")
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

    def on_type_changed(self):
        self.populate_sizes()

    def get_current_sizes(self):
        if self.equal_radio.isChecked():
            return equal_angles
        return unequal_angles

    def populate_sizes(self):
        sizes = self.get_current_sizes()
        self.size_table.setRowCount(len(sizes))
        for row, size_data in enumerate(sizes):
            for col, value in enumerate(size_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
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
            QtWidgets.QMessageBox.warning(self, "Warning", "Please select a size.")
            return
        super().accept()


def create_l_angle(size_data, length, angle_type="equal", mirror=False):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()
    
    body = doc.addObject('PartDesign::Body', 'LAngleBody')

    name = f"LAngle_Sketch"
    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = size_data[0].split('x')

    x_factor = -1 if mirror else 1

    points = [
        [0, 0],
        [0, float(dimensions[0])],
        [float(dimensions[2]) * x_factor, float(dimensions[0])],
        [float(dimensions[2]) * x_factor, float(dimensions[2])],
        [float(dimensions[1]) * x_factor, float(dimensions[2])],
        [float(dimensions[1]) * x_factor, 0],
    ]

    for i, pt in enumerate(points):
        x1, y1 = pt
        x2, y2 = points[(i + 1) % len(points)]
        p1 = Vector(x1, y1, 0)
        p2 = Vector(x2, y2, 0)
        
        current_sketch.addGeometry(Part.LineSegment(p1, p2), False)

    pad = body.newObject('PartDesign::Pad', "TubePad")
    pad.Type = "Length" 
    pad.Profile = current_sketch
    pad.Length = length
    pad.Reversed = False
    pad.Midplane = False
    body.recompute()

    current_sketch.Visibility = False

    body.Tip = pad
    doc.recompute()
