def solution(mats, park):
    mats.sort(reverse=True)
    len_x, len_y = len(park), len(park[0])
    for l in mats:
        for x in range(len_x - l + 1):
            for y in range(len_y - l + 1):
                for i in range(l**2):
                    if park[x+i%l][y+i//l] != "-1":
                        break
                else:
                    return l
    return -1