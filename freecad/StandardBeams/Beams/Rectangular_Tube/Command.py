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
                createBeam(size_data, length)

        except Exception:
            Console.PrintError("Rectangular Tube error\n")

    def GetResources(self):
        return {
            "MenuText": "Rectangular Tube",
            "ToolTip": "Create a standard Rectangular Tube profile",
            "Pixmap": asIcon('Rectangular-Tube'),
        }

    def IsActive(self):
        return True
