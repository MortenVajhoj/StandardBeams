# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from ...Misc.Imprint import imprint
from .Standard import round_tube_standards , load_round_tube_sizes


def createBeam(size_data, length, standard_name="European (EN 10210-2 CHS)"):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()

    folder, beams_csv, sizes_csv = round_tube_standards[standard_name]
    round_tube_sizes = load_round_tube_sizes(folder, sizes_csv)

    body = doc.addObject('PartDesign::Body', 'RoundTubeBody')

    imprint(body)

    name = f"RoundTube_Sketch"

    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = round_tube_sizes.get(size_data[0])
    outer_diameter = dimensions[0]
    inner_diameter = outer_diameter - 2 * dimensions[1]

    center = Vector(0, 0, 0)
    current_sketch.addGeometry(Part.Circle(center, Vector(0, 0, 1), outer_diameter / 2), False)
    current_sketch.addGeometry(Part.Circle(center, Vector(0, 0, 1), inner_diameter / 2), False)

    pad = body.newObject('PartDesign::Pad', "TubePad")
    pad.Type = "Length"
    pad.Profile = current_sketch
    pad.Length = length

    current_sketch.Visibility = False

    doc.recompute()