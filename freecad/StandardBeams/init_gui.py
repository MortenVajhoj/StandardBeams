# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.


import FreeCADGui as Gui
import FreeCAD
import os

from .Misc.Resources import asIcon


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

        except Exception as exception:
            print(exception)
            FreeCAD.Console.PrintError("I-Beam error\n")

    def GetResources(self):
        return {
            "MenuText": "I-Beam",
            "ToolTip": "Create a standard I-Beam profile",
            "Pixmap": asIcon('I-Beam'),
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

        except Exception as exception:
            print(exception)
            FreeCAD.Console.PrintError("L-Angle error\n")

    def GetResources(self):
        return {
            "MenuText": "L-Angle",
            "ToolTip": "Create a standard L-Angle profile",
            "Pixmap": asIcon('L-Angle'),
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
            FreeCAD.Console.PrintError("Rectangular Tube error\n")

    def GetResources(self):
        return {
            "MenuText": "Rectangular Tube",
            "ToolTip": "Create a standard Rectangular Tube profile",
            "Pixmap": asIcon('Rectangular-Tube'),
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

        except Exception as exception:
            print(exception)
            FreeCAD.Console.PrintError("Square Tube error\n")

    def GetResources(self):
        return {
            "MenuText": "Square Tube",
            "ToolTip": "Create a standard Square Tube profile",
            "Pixmap": asIcon('Square-Tube'),
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

        except Exception as exception:
            print(exception)
            FreeCAD.Console.PrintError("Round Tube error\n")

    def GetResources(self):
        return {
            "MenuText": "Round Tube",
            "ToolTip": "Create a standard Round Tube profile",
            "Pixmap": asIcon('Round-Tube'),
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


Gui.addWorkbench(StandardBeamsWorkbench())
