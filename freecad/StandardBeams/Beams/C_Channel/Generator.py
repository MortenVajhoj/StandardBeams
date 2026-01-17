# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from ...Misc.Imprint import imprint
from .Standard import C_channel_standards , load_c_channel_sizes


def createBeam(size_data, length, standard_name="UAP Channel"):

    import FreeCAD
    import Part
    from FreeCAD import Placement, Rotation, Vector

    doc = FreeCAD.ActiveDocument
    if doc is None:
        doc = FreeCAD.newDocument()

    folder, channels_csv, sizes_csv = C_channel_standards[standard_name]
    c_channel_sizes = load_c_channel_sizes(folder, sizes_csv)

    body = doc.addObject('PartDesign::Body', 'CChannelBody')

    imprint(body)

    name = f"CChannel_Sketch"
    current_sketch = body.newObject('Sketcher::SketchObject', name)
    current_sketch.Placement = FreeCAD.Placement(FreeCAD.Vector(0, 0, 0), FreeCAD.Rotation(0, 0, 0, 1))

    dimensions = c_channel_sizes.get(size_data[0])

    points = [
        [0, 0],
        [dimensions[1], 0],
        [dimensions[1], dimensions[3]],
        [dimensions[2], dimensions[3]],
        [dimensions[2], dimensions[0] - dimensions[3]],
        [dimensions[1], dimensions[0] - dimensions[3]],
        [dimensions[1], dimensions[0]],
        [0, dimensions[0]],
    ]

    for i, pt in enumerate(points):
        x1, y1 = pt
        x2, y2 = points[(i + 1) % len(points)]
        p1 = Vector(x1, y1, 0)
        p2 = Vector(x2, y2, 0)

        current_sketch.addGeometry(Part.LineSegment(p1, p2), False)

    pad = body.newObject('PartDesign::Pad', "CChannelPad")
    pad.Type = "Length"
    pad.Profile = current_sketch
    pad.Length = length

    current_sketch.Visibility = False

    body.recompute()
    body.Tip = pad
    doc.recompute()
