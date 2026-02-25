def generate_explanations(layout):
    explanations = []

    if any(r.type == "living" and r.y == 0 for r in layout):
        explanations.append(
            "Living room placed near entrance for easy access"
        )

    if all(r.type != "bedroom" or r.y > 10 for r in layout):
        explanations.append(
            "Bedrooms placed in rear area for better privacy"
        )

    if any(r.type == "kitchen" for r in layout):
        explanations.append(
            "Kitchen positioned close to living for convenience"
        )

    if any(r.type == "bathroom" for r in layout):
        explanations.append(
            "Bathrooms located near private zones"
        )

    return explanations