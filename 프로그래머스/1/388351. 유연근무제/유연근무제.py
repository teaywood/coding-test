def solution(schedules, timelogs, startday):
    result = 0
    for goal, log in zip(schedules, timelogs):
        
        goal += 10 #출근 희망 시간 + 10분
        
        #시간이 바뀌는 예외 처리
        if (goal % 100) >= 60:
            goal += 40
        
        #평일에 한해 출근 여부 계산
        for idx, time in enumerate(log):
            if ((startday + idx - 1) % 7 + 1) not in (6, 7) and time > goal:
                break
        else:
            result += 1
            
    return result
