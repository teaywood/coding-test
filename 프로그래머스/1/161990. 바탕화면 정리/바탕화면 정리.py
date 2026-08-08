def solution(wallpaper):
    luy = len(wallpaper[0]) #초기값: max y idx
    lux = rdx = rdy = -1

    for x, arr in enumerate(wallpaper):
        for y, doc in enumerate(arr):
            if doc == '#':
                #가장 위 좌표 찾기
                if lux == -1:
                    lux = x
                #가장 왼쪽 좌표 찾기
                if y < luy:
                    luy = y
                #가장 아래 좌표 찾기
                if x+1 > rdx:
                    rdx = x+1
                #가장 오른쪽 좌표 찾기
                if y+1 > rdy:
                    rdy = y+1
            
    return [lux, luy, rdx, rdy]