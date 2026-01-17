# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from ...Misc.Imprint import imprint


def createBeam(size_data, length):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()

    body = doc.addObject('PartDesign::Body', 'RoundTubeBody')

    imprint(body)

    name = f"RoundTube_Sketch"

    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = size_data[0].partition('x')
    outer_diameter = float(dimensions[0])
    inner_diameter = outer_diameter - 2 * float(dimensions[2])

    center = Vector(0, 0, 0)
    current_sketch.addGeometry(Part.Circle(center, Vector(0, 0, 1), outer_diameter / 2), False)
    current_sketch.addGeometry(Part.Circle(center, Vector(0, 0, 1), inner_diameter / 2), False)

    pad = body.newObject('PartDesign::Pad', "TubePad")
    pad.Type = "Length"
    pad.Profile = current_sketch
    pad.Length = length
    pad.Reversed = False
    pad.Midplane = False

    current_sketch.Visibility = False

    doc.recompute()