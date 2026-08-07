def solution(numbers, hand):
    result = []
    l_hand, r_hand = 10, 12 #왼손, 오른손 위치 (* 0 # -> 10 11 12) 보정
    
    for n in numbers:
        if n == 0:
            n = 11
        if n in (1, 4, 7):
            result.append("L")
            l_hand = n
        elif n in (3, 6, 9):
            result.append("R")
            r_hand = n
        else:
            l_diff = sum(divmod(abs(l_hand - n), 3))
            r_diff = sum(divmod(abs(r_hand - n), 3))
            
            #거리 같을 시 주 손에 따라 보정 처리
            if l_diff == r_diff:
                if hand[0] == "l":
                    r_diff += 1
                else:
                    l_diff += 1
                    
            if l_diff < r_diff:
                result.append("L")
                l_hand = n
            elif l_diff > r_diff:
                result.append("R")
                r_hand = n

    return "".join(result)
