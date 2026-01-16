# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.


import FreeCADGui as Gui
import FreeCAD
import os

class IBeam:
    def Activated(self):
        from PySide import QtWidgets
        from .scripts.i_beam import IBeamDialog, create_i_beam

        try:
            parent = QtWidgets.QApplication.activeWindow()
            dialog = IBeamDialog(parent=parent)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                size_data = dialog.get_selected_size()
                length = dialog.get_length()
                standard = dialog.current_standard
                create_i_beam(size_data, length, standard)

        except Exception:
            FreeCAD.Console.PrintError("I-Beam error")

    def GetResources(self):
        icon = os.path.join(os.path.dirname(__file__), "icons", "IBeam.svg")
        return {
            "MenuText": "I-Beam",
            "ToolTip": "Create a standard I-Beam profile",
            "Pixmap": icon,
        }
    
    def IsActive(self):
        return True


class LAngle:
    def Activated(self):
        from PySide import QtWidgets
        from .scripts.l_angle import LAngleDialog, create_l_angle

        try:
            parent = QtWidgets.QApplication.activeWindow()
            dialog = LAngleDialog(parent=parent)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                size_data = dialog.get_selected_size()
                length = dialog.get_length()
                angle_type = dialog.get_angle_type()
                mirror = dialog.get_mirror()
                create_l_angle(size_data, length, angle_type, mirror)

        except Exception:
            FreeCAD.Console.PrintError("L-Angle error")

    def GetResources(self):
        icon = os.path.join(os.path.dirname(__file__), "icons", "LAngle.svg")
        return {
            "MenuText": "L-Angle",
            "ToolTip": "Create a standard L-Angle profile",
            "Pixmap": icon,
        }
    
    def IsActive(self):
        return True


class RectangularTube:
    def Activated(self):
        from PySide import QtWidgets
        from .scripts.rectangular_tube import RectangularTubeDialog, create_rectangular_tube

        try:
            parent = QtWidgets.QApplication.activeWindow()
            dialog = RectangularTubeDialog(parent=parent)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                size_data = dialog.get_selected_size()
                length = dialog.get_length()
                create_rectangular_tube(size_data, length)

        except Exception:
            FreeCAD.Console.PrintError("Rectangular Tube error")

    def GetResources(self):
        icon = os.path.join(os.path.dirname(__file__), "icons", "RectTube.svg")
        return {
            "MenuText": "Rectangular Tube",
            "ToolTip": "Create a standard Rectangular Tube profile",
            "Pixmap": icon,
        }
    
    def IsActive(self):
        return True


class SquareTube:
    def Activated(self):
        from PySide import QtWidgets
        from .scripts.square_tube import SquareTubeDialog, create_square_tube

        try:
            parent = QtWidgets.QApplication.activeWindow()
            dialog = SquareTubeDialog(parent=parent)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                size_data = dialog.get_selected_size()
                length = dialog.get_length()
                create_square_tube(size_data, length)

        except Exception:
            FreeCAD.Console.PrintError("Square Tube error")

    def GetResources(self):
        icon = os.path.join(os.path.dirname(__file__), "icons", "SquareTube.svg")
        return {
            "MenuText": "Square Tube",
            "ToolTip": "Create a standard Square Tube profile",
            "Pixmap": icon,
        }
    
    def IsActive(self):
        return True


class RoundTube:
    def Activated(self):
        from PySide import QtWidgets
        from .scripts.round_tube import RoundTubeDialog, create_round_tube

        try:
            parent = QtWidgets.QApplication.activeWindow()
            dialog = RoundTubeDialog(parent=parent)
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                size_data = dialog.get_selected_size()
                length = dialog.get_length()
                create_round_tube(size_data, length)

        except Exception:
            FreeCAD.Console.PrintError("Round Tube error")

    def GetResources(self):
        icon = os.path.join(os.path.dirname(__file__), "icons", "RoundTube.svg")
        return {
            "MenuText": "Round Tube",
            "ToolTip": "Create a standard Round Tube profile",
            "Pixmap": icon,
        }
    
    def IsActive(self):
        return True




Gui.addCommand("IBeamCommand", IBeam())
Gui.addCommand("LAngleCommand", LAngle())
Gui.addCommand("RectangularTubeCommand", RectangularTube())
Gui.addCommand("SquareTubeCommand", SquareTube())
Gui.addCommand("RoundTubeCommand", RoundTube())

class StandardBeamsWorkbench(Gui.Workbench):
    MenuText = "Standard Beams"
    ToolTip = "Tools for creating standard structural beam profiles"

    @property
    def Icon(self):
        return os.path.join(os.path.dirname(__file__), "icons", "IBeam.svg")

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


Gui.addWorkbench(StandardBeamsWorkbench())
