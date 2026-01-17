# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

import csv
import os


round_tube_standards = {
    "European (EN 10210-2 CHS)": ("European", "Round-Tubes.csv"),
}

def get_csv_path(folder, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, '..','..', 'Resources','Standards', folder, filename)

def load_round_tubes(folder, filename):
    csv_path = get_csv_path(folder, filename)
    tubes = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                tubes.append(row)
    return tubes


