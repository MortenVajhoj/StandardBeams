# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

def Area_property(size_data):
    h, b, t, s = size_data
    return 2 * (b * t) + (h - 2 * t) * s

def Moment_of_Inertia_X_property(size_data):
    h, b, t, s = size_data
    return round((b * h**3 - (b - s) * (h - 2*t)**3) / 12, -3)

def Moment_of_Inertia_Y_property(size_data):
    h, b, t, s = size_data
    I_flanges = (t * b**3) / 6
    
    I_web = ((h - 2 * t) * s**3) / 12
    
    return round(I_flanges + I_web, -3)