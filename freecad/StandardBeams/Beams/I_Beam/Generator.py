# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from ...Misc.Imprint import imprint
from .Standard import I_beam_standards , load_i_beam_sizes


def createBeam(size_data, length, standard_name="European (EN 10365)"):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()

    folder, beams_csv, sizes_csv = I_beam_standards[standard_name]
    I_beam_sizes = load_i_beam_sizes(folder, sizes_csv)

    body = doc.addObject('PartDesign::Body', 'IBeamBody')

    imprint(body)

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
