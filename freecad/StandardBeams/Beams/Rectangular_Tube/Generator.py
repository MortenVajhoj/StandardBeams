# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from ...Misc.Imprint import imprint
from .Standard import rectangular_tube_standards , load_rectangular_tube_sizes


def createBeam(size_data, length, standard_name="European (EN 10210-2 RHS)"):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()

    folder, beams_csv, sizes_csv = rectangular_tube_standards[standard_name]
    rectangular_tube_sizes = load_rectangular_tube_sizes(folder, sizes_csv)

    body = doc.addObject('PartDesign::Body', 'RectangularTubeBody')

    imprint(body)

    name = f"RectangularTube_Sketch"

    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = rectangular_tube_sizes.get(size_data[0])
    outer_points = [
        [0, 0],
        [0, dimensions[0]],
        [dimensions[1], dimensions[0]],
        [dimensions[1], 0],
    ]

    inner_points = [
        [dimensions[2], dimensions[2]],
        [dimensions[2], dimensions[0] - dimensions[2]],
        [dimensions[1] - dimensions[2], dimensions[0] - dimensions[2]],
        [dimensions[1] - dimensions[2], dimensions[2]],
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

    current_sketch.Visibility = False

    body.recompute()
    body.Tip = pad
    doc.recompute()
