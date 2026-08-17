def solution(video_len, pos, op_start, op_end, commands):
    
    #분 -> 초 변환 함수
    def eval_sec(time):
        time_split = list(map(int, time.split(":")))
        min_to_sec = time_split[0] * 60 + time_split[1]
        return min_to_sec
    
    v_len = eval_sec(video_len)
    p = eval_sec(pos)
    op_s = eval_sec(op_start)
    op_e = eval_sec(op_end)
    
    for c in commands:
        #오프닝 건너뛰기 
        if op_s <= p <= op_e:
            p = op_e
        #next
        if c == "next":
            p += 10
        else: #prev
            p -= 10
            
        #경계값 처리
        if p < 0: p = 0
        if p > v_len: p = v_len
        
    #마지막 오프닝 건너뛰기 
    if op_s <= p <= op_e:
        p = op_e
        
    return f"{p//60:02d}" + ":" +  f"{p%60:02d}"