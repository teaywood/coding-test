def solution(players, callings):
    name_index = {name:idx for idx, name in enumerate(players)}
    for name in callings:
        idx = name_index[name]
        name_index[players[idx-1]] += 1
        name_index[name] -= 1
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players