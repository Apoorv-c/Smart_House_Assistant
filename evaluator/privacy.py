def privacy_score(layout):
    score = 100

    living = next((r for r in layout if r.type == "living"), None)
    if not living:
        return 50

    for r in layout:
        if r.type == "bedroom":
            if r.y <= living.height:
                score -= 15

        if r.type == "bathroom":
            if r.y < living.height:
                score -= 10

    return max(score, 0)