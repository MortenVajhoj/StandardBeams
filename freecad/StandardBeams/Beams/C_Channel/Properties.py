# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

def Area_property(size_data):
    return size_data[1] * size_data[2] * 2 + (size_data[0] - 2 * size_data[2]) * size_data[3]

def Moment_of_Inertia_X_property(size_data):
    h, b, t, s = size_data
    return round((b * h**3 - (b - s) * (h - 2*t)**3) / 12, -3)

def Centroid_X(size_data):
    h, b, t, s = size_data
    
    A_web_full = h * s
    x_web = s / 2
    
    A_flange_overhangs = 2 * (t * (b - s)) 
    x_flange = s + (b - s) / 2
    
    Total_Area = A_web_full + A_flange_overhangs
    
    return (A_web_full * x_web + A_flange_overhangs * x_flange) / Total_Area

def Moment_of_Inertia_Y_property(size_data):
    h, b, t, s = size_data
    
    cx = Centroid_X(size_data)
    
    I_web_local = (h * s**3) / 12
    A_web = h * s
    d_web = cx - (s / 2)
    I_web_total = I_web_local + A_web * d_web**2
    
    width_overhang = b - s
    I_flange_local = (t * width_overhang**3) / 12
    A_flange = t * width_overhang
    x_overhang_center = s + width_overhang / 2
    d_flange = x_overhang_center - cx
    
    I_flanges_total = 2 * (I_flange_local + A_flange * d_flange**2)
    
    return round(I_web_total + I_flanges_total, -3)