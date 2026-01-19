# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

def Area_property(size_data):
    h, b, t = size_data

    outer_area = h * b
    inner_area = (h - 2*t) * (b - 2*t)
    
    return outer_area - inner_area

def Moment_of_Inertia_X_property(size_data):
    h, b, t = size_data
    
    I_outer = (b * h**3) / 12
    
    I_inner = ((b - 2*t) * (h - 2*t)**3) / 12
    
    return round(I_outer - I_inner, -3)

def Moment_of_Inertia_Y_property(size_data):
    h, b, t = size_data
    
    I_outer = (h * b**3) / 12
    
    I_inner = ((h - 2*t) * (b - 2*t)**3) / 12
    
    return round(I_outer - I_inner, -3)