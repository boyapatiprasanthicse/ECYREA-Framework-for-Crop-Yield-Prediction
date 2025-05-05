def optimize_fertilizer(nutrient_data):
    if nutrient_data['N'] < 50:
        return 'Add Nitrogen'
    return 'Balanced'
