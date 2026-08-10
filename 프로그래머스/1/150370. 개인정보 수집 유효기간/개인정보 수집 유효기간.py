def solution(today, terms, privacies):
    term_box = {}
    td_y, td_m, td_d = map(int, today.split('.'))
    result = []
    
    for k in terms:
        tmp = k.split(' ')
        term_box[tmp[0]] = int(tmp[1])
    
    for idx, day in enumerate(privacies):
        day, term = day.split(' ')
        y, m, d = list(map(int, day.split('.')))
        
        m += term_box[term]
        d -= 1
        if d == 0:
            d = 28
            m -= 1
        if m > 12:
            y += (m-1) // 12
            m = (m-1) % 12 + 1

        if td_y > y:
            result.append(idx+1)
            continue
        elif td_y == y:
            if td_m > m:
                result.append(idx+1)
                continue
            elif td_m == m and td_d > d:
                result.append(idx+1)
                continue
        
    return result