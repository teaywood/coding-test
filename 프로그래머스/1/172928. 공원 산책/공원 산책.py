def solution(park, routes):
    vec = {"N":(-1, 0), "S":(1, 0), "W":(0, -1), "E":(0, 1)}
    x_limit, y_limit = len(park), len(park[0])
    
    #시작 좌표 추출
    start = [(x, y) for x, arr in enumerate(park) for y, start in enumerate(arr) if start == "S"]
    x, y = start[0]
    
    for route in routes:
        op, n = route.split(' ') # routes 방향 / 거리 추출
        n = int(n)
        dx, dy = vec[op]
        
        for i in range(1, n+1):
            check_x, check_y = x + (dx * i), y + (dy * i)
            if not (0 <= check_x < x_limit): # 길을 벗어나는지 확인
                break
            if not (0 <= check_y < y_limit): # 길을 벗어나는지 확인
                break
            if park[check_x][check_y] == "X": # 장애물 지나가는지 확인
                break
        else:
            x, y = x + (dx * n), y + (dy * n)
    return [x, y]




