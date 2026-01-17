# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

import csv
import os


l_angle_standards = {
    "European (EN 10210-2 Equal)": ("European", "Properties/Equal-Angles.csv", "Sizes/Equal-Angle-Sizes.csv"),
    "European (EN 10210-2 Unequal)": ("European", "Properties/Unequal-Angles.csv", "Sizes/Unequal-Angle-Sizes.csv"),
}


def get_csv_path(folder, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, '..','..', 'Resources','Standards', folder, filename)

def load_l_angles(folder, filename):
    csv_path = get_csv_path(folder, filename)
    angles = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                angles.append(row)
    return angles


def load_l_angle_sizes(folder, filename):
    csv_path = get_csv_path(folder, filename)
    sizes = {}
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 4:
                name = row[0]
                sizes[name] = [float(row[1]), float(row[2]), float(row[3])]
    return sizes


