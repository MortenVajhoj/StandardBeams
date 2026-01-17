# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

import csv
import os


C_channel_standards = {
    "UAP Channel": ("European", "Properties/UAP-Channels.csv", "Sizes/UAP-Channel-Sizes.csv"),
    "UPE Channel ": ("European", "Properties/UPE-Channels.csv", "Sizes/UPE-Channel-Sizes.csv"),
    "UPN Channel": ("European", "Properties/UPN-Channels.csv", "Sizes/UPN-Channel-Sizes.csv")
}

def get_csv_path(folder, filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, '..','..', 'Resources','Standards', folder, filename)

def load_c_channels(folder, filename):
    csv_path = get_csv_path(folder, filename)
    beams = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                beams.append(row)
    return beams


def load_c_channel_sizes(folder, filename):
    csv_path = get_csv_path(folder, filename)
    sizes = {}
    with open(csv_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row and len(row) >= 5:
                name = row[0]
                sizes[name] = [float(row[1]), float(row[2]), float(row[3]), float(row[4])]
    return sizes
