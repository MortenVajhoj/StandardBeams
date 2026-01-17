# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

from .Version import Version


def imprint ( object ):

    def add ( name : str ):

        object.addProperty(
            read_only = True ,
            hidden = True ,
            group = 'Addon' ,
            attr = 8 , # Output
            type = 'App::PropertyString' ,
            name = f'Addon_{ name }'
        )

    add('Version')
    add('Origin')

    object.Addon_Version = Version
    object.Addon_Origin = 'StandardBeams'
