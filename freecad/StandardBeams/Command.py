# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from FreeCAD import Gui

from .Beams import (
    RectangularTubeCommand ,
    SquareTubeCommand ,
    RoundTubeCommand ,
    LAngleCommand ,
    IBeamCommand
)


def registerCommands ():

    Gui.addCommand('StandardBeams_Rectangular-Tube',RectangularTubeCommand())
    Gui.addCommand('StandardBeams_Square-Tube',SquareTubeCommand())
    Gui.addCommand('StandardBeams_Round-Tube',RoundTubeCommand())
    Gui.addCommand('StandardBeams_L-Angle',LAngleCommand())
    Gui.addCommand('StandardBeams_I-Beam',IBeamCommand())