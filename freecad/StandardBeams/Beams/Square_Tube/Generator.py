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
