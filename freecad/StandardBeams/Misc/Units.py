# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileNotice: Part of the Standard Beams addon.

mm_headers = {
    "i_beam": ["Shape", "Height (mm)", "Width (mm)", "Flange (mm)", "Web (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
    "h_beam": ["Shape", "Height (mm)", "Width (mm)", "Flange (mm)", "Web (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
    "c_channel": ["Shape", "Height (mm)", "Width (mm)", "Flange (mm)", "Web (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
    "l_angle": ["Shape", "Height (mm)", "Width (mm)", "Thickness (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
    "rectangular_tube": ["Shape", "Height (mm)", "Width (mm)", "Thickness (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
    "square_tube": ["Shape", "Height (mm)", "Width (mm)", "Thickness (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
    "round_tube": ["Shape", "Outer Diameter (mm)", "Wall Thickness (mm)", "Area (mm²)", "Moment of Inertia X (mm⁴)", "Moment of Inertia Y (mm⁴)"],
}

inch_headers = {
    "i_beam": ["Shape", "Height (in)", "Width (in)", "Flange (in)", "Web (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
    "h_beam": ["Shape", "Height (in)", "Width (in)", "Flange (in)", "Web (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
    "c_channel": ["Shape", "Height (in)", "Width (in)", "Flange (in)", "Web (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
    "l_angle": ["Shape", "Height (in)", "Width (in)", "Thickness (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
    "rectangular_tube": ["Shape", "Height (in)", "Width (in)", "Thickness (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
    "square_tube": ["Shape", "Height (in)", "Width (in)", "Thickness (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
    "round_tube": ["Shape", "Outer Diameter (in)", "Wall Thickness (in)", "Area (in²)", "Moment of Inertia X (in⁴)", "Moment of Inertia Y (in⁴)"],
}


def is_american_standard(folder):
    return folder == "American"


def get_unit_suffix(folder):
    return " in" if is_american_standard(folder) else " mm"


def get_table_headers(folder, beam_type):
    """Get the appropriate table headers based on folder and beam type."""
    if is_american_standard(folder):
        return inch_headers.get(beam_type, inch_headers["i_beam"])
    return mm_headers.get(beam_type, mm_headers["i_beam"])


def get_column_count(beam_type):
    """Get the number of columns for a beam type."""
    return len(mm_headers.get(beam_type, mm_headers["i_beam"]))


def convert_dimensions_to_mm(dimensions, folder):
    if not is_american_standard(folder):
        return dimensions
    
    return [dim * 25.4 for dim in dimensions]


def convert_length_to_mm(length, folder):
    if not is_american_standard(folder):
        return length
    
    return length * 25.4
