# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from .Misc.Resources import asIcon
from FreeCAD import Gui


class StandardBeamsWorkbench(Gui.Workbench):
    MenuText = "Standard Beams"
    ToolTip = "Tools for creating standard structural beam profiles"

    @property
    def Icon(self):
        return asIcon('I-Beam')

    def Initialize(self):

        cmds = [
            "IBeamCommand",
            "LAngleCommand",
            "RectangularTubeCommand",
            "SquareTubeCommand",
            "RoundTubeCommand",
        ]

        self.appendToolbar("Standard Beams Tools", cmds)
        self.appendMenu("Standard Beams", cmds)

    def Activated(self):
        pass

    def Deactivated(self):
        pass

    def ContextMenu(self, recipient):
        if recipient == "view":
            self.appendContextMenu("Standard Beams", [
                "IBeamCommand",
                "LAngleCommand",
                "SquareTubeCommand",
                "RectangularTubeCommand",
                "RoundTubeCommand",
            ])

    def GetClassName(self):
        return "Gui::PythonWorkbench"