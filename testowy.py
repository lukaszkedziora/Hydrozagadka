    if key == "W":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][0] -= 1
    elif key == "A":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][1] -= 1
    elif key == "S":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][0] += 1
    elif key == "D":
        characters[boards[player['board']]['characters'][1]]['position'][player['board']][1] += 1