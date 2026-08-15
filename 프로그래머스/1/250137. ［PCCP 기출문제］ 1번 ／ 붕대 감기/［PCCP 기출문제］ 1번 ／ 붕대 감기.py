def solution(bandage, health, attacks):
    attacks_time, attacks_damage = list(zip(*attacks))
    s_count = 0
    max_health = health

    for t in range(1, attacks_time[-1]+1):
        # 피격 체크
        if t in attacks_time:
            health -= attacks_damage[attacks_time.index(t)]
            s_count = 0
            if health <= 0:
                return -1
            continue
            
        # 체력 회복
        health += bandage[1]
        s_count += 1
        if s_count == bandage[0]:
            health += bandage[2]
            s_count = 0
        
        # 체력 초과 예외처리
        health = min(max_health, health)
    return health
