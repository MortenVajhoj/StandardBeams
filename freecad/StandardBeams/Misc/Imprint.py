
from FreeCAD import PropertyType

from .Version import Version


def imprint ( object ):

    def add ( name : str ):

        object.addProperty(
            read_only = True ,
            hidden = True ,
            group = 'Addon' ,
            attr = PropertyType.Prop_Hidden ,
            type = 'App::PropertyString' ,
            name = f'Addon_{ name }'
        )

    add('Version')
    add('Origin')

    object.Addon_Version = Version
    object.Addon_Origin = 'StandardBeams'
