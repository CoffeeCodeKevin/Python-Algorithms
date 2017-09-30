def tickets(people):
    change = {
        "25s": 0,
        "50s": 0,
        "100s": 0,
    }
    for i in people:
        if i == 25:
            change["25s"] += 1
            for j in change.values():
                if j < 0:
                    return "NO"
        if i == 50:
            change["50s"] += 1
            change["25s"] -= 1
            for j in change.values():
                if j < 0:
                    return "NO"
        if i == 100:
            change["100s"] += 1
            if change["50s"] == 0 and change["25s"] >= 3:
                change["25s"] -= 3
            else:
                change["50s"] -= 1
                change["25s"] -= 1
            for j in change.values():
                if j < 0:
                    return "NO"
    return "YES"
