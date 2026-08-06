def solution(triangle):
    reversed_triangle = triangle[::-1].copy()
    l = len(triangle)
    
    for idx in range(l):
        tmp = []
        floor = reversed_triangle[idx]
        for i in range(len(floor)-1):
            max_bottom = max(floor[i], floor[i+1])
            top_num = reversed_triangle[idx+1][i]
            tmp.append(max_bottom + top_num)
        if idx+1 == l:
            break
        reversed_triangle[idx+1] = tmp.copy()
    return reversed_triangle[-1][0]
            
#아래 두 개중 큰 걸 골라서, 위에거와 더함 그걸 위에층의 리스트로 사용
    
    
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

#
#
# 8+(7,12) 1+(12,10) 0+(10,10)
# 2+(4,5) 7+(5,2)
# 4 5 2 6 5



# 7 = 30
# 23 21
# 20 13 10
# 7 12 10 10
# 