# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from ...Misc.Resources import asIcon
from ...Qt.Widgets import QApplication , QDialog

from .Generator import createBeam
from .Dialog import Dialog

from FreeCAD import Console


class Command:
    def Activated(self):

        try:
            parent = QApplication.activeWindow()
            dialog = Dialog(parent=parent)
            if dialog.exec_() == QDialog.DialogCode.Accepted:
                size_data = dialog.get_selected_size()
                length = dialog.get_length()
                standard = dialog.current_standard
                createBeam(size_data, length, standard)

        except Exception as exception:
            print(exception)
            Console.PrintError("L-Angle error\n")

    def GetResources(self):
        return {
            "MenuText": "L-Angle",
            "ToolTip": "Create a standard L-Angle profile",
            "Pixmap": asIcon('L-Angle'),
        }

    def IsActive(self):
        return True