
def calculate_body_type(measurement):

    bust = measurement.bust
    waist = measurement.waist
    hips = measurement.hips

    if waist == 0:
        return "unknown"

    waist_hip_ratio = waist / hips
    bust_waist_ratio = bust / waist

    if waist_hip_ratio < 0.75 and bust_waist_ratio > 1.2:
        return "hourglass"
    elif hips > bust + 5:  # 5cm tolerance
        return "pear"
    elif bust > hips + 5:
        return "inverted_triangle"
    elif abs(bust - hips) < 5 and waist_hip_ratio > 0.8:
        return "rectangle"
    else:
        return "apple"