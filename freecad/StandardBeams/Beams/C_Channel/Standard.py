# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

import csv
import os
from .Properties import Area_property, Moment_of_Inertia_X_property, Moment_of_Inertia_Y_property


C_channel_standards = {
    "UAP (EN 10365)": ("European", "UAP-Channel-Sizes.csv"),
    "UPE (EN 10365)": ("European", "UPE-Channel-Sizes.csv"),
    "UPN (EN 10365)": ("European", "UPN-Channel-Sizes.csv"),
}

def get_csv_path(folder, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, '..','..', 'Resources','Standards', folder, filename)

def load_c_channel_sizes(folder, filename):
    csv_path = get_csv_path(folder, filename)
    sizes = []
    sizes_dict = {}
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 5:
                name = row[0]
                h = float(row[1])
                b = float(row[2])
                tf = float(row[3])
                tw = float(row[4])
                
                size_data = [h, b, tf, tw]
                
                area = Area_property(size_data)
                ix = Moment_of_Inertia_X_property(size_data)
                iy = Moment_of_Inertia_Y_property(size_data)
                
                row.append(f"{area:.2f}")
                row.append(f"{ix:.2f}")
                row.append(f"{iy:.2f}")
                
                sizes.append(row)
                sizes_dict[name] = size_data
    return sizes, sizes_dict
