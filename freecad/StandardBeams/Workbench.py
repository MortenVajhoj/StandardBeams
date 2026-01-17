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
            'StandardBeams_I-Beam' ,
            'StandardBeams_L-Angle' ,
            'StandardBeams_Rectangular-Tube' ,
            'StandardBeams_Square-Tube' ,
            'StandardBeams_Round-Tube'
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
                'StandardBeams_I-Beam' ,
                'StandardBeams_L-Angle' ,
                'StandardBeams_Rectangular-Tube' ,
                'StandardBeams_Square-Tube' ,
                'StandardBeams_Round-Tube'
            ])

    def GetClassName(self):
        return "Gui::PythonWorkbench"