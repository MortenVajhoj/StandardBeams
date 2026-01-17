# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from .Workbench import StandardBeamsWorkbench
from .Command import registerCommands

from FreeCAD import Gui


registerCommands()

Gui.addWorkbench(StandardBeamsWorkbench())
