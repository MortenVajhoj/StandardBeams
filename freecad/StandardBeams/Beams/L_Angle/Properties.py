# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

def Area_property(size_data):
    h, b, t = size_data
    return (h * t) + (b - t) * t

def Centroid_Y(size_data):
    h, b, t = size_data
    
    A1 = h * t
    y1 = h / 2
    
    A2 = (b - t) * t
    y2 = t / 2
    
    return (A1 * y1 + A2 * y2) / (A1 + A2)

def Moment_of_Inertia_X_property(size_data):
    h, b, t = size_data
    
    cy = Centroid_Y(size_data)

    A1 = h * t
    I_local_1 = (t * h**3) / 12
    d1 = (h / 2) - cy
    I_part1 = I_local_1 + A1 * d1**2

    A2 = (b - t) * t
    I_local_2 = ((b - t) * t**3) / 12
    d2 = (t / 2) - cy
    I_part2 = I_local_2 + A2 * d2**2
    
    return round(I_part1 + I_part2, -3)

def Centroid_X(size_data):
    h, b, t = size_data
    
    A1 = h * t
    x1 = t / 2
    
    A2 = (b - t) * t

    x2 = t + (b - t) / 2 
    
    return (A1 * x1 + A2 * x2) / (A1 + A2)

def Moment_of_Inertia_Y_property(size_data):
    h, b, t = size_data
    
    cx = Centroid_X(size_data)
    
    A1 = h * t
    I_local_1 = (h * t**3) / 12
    d1 = (t / 2) - cx
    I_part1 = I_local_1 + A1 * d1**2

    A2 = (b - t) * t
    I_local_2 = (t * (b - t)**3) / 12
    x2 = t + (b - t) / 2
    d2 = x2 - cx
    I_part2 = I_local_2 + A2 * d2**2
    
    return round(I_part1 + I_part2, -3)