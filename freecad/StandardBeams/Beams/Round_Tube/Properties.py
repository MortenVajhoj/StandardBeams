# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

import math

def Area_property(size_data):
    D, t = size_data
    
    d = D - 2 * t

    return (math.pi * (D**2 - d**2)) / 4

def Moment_of_Inertia_X_property(size_data):
    D, t = size_data

    d = D - 2 * t
    
    return round((math.pi * (D**4 - d**4)) / 64, -3)

def Moment_of_Inertia_Y_property(size_data):
    return Moment_of_Inertia_X_property(size_data)