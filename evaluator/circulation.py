def circulation_score(layout):
    score = 60

    living = next((r for r in layout if r.type == "living"), None)
    kitchen = next((r for r in layout if r.type == "kitchen"), None)

    if living and kitchen:
        distance = abs(kitchen.x - (living.x + living.width))
        if distance < 3:
            score += 20

    return min(score, 100)