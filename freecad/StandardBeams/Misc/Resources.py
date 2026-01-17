# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the StandardBeams addon.

import freecad.StandardBeams as module
from importlib import resources


icons = resources.files(module) / 'Resources/Icons'


def asIcon ( name : str ):

    file = name + '.svg'

    icon = icons / file

    with resources.as_file(icon) as path:
        return str( path )