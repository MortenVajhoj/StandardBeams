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

    Gui.addCommand('RectangularTubeCommand',RectangularTubeCommand())
    Gui.addCommand('SquareTubeCommand',SquareTubeCommand())
    Gui.addCommand('RoundTubeCommand',RoundTubeCommand())
    Gui.addCommand('LAngleCommand',LAngleCommand())
    Gui.addCommand('IBeamCommand',IBeamCommand())