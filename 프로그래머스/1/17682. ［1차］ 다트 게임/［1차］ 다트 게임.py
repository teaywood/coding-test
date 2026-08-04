def solution(dartResult):
    point = []
    bonus_box = {"S":1, "D":2, "T":3}
    #10을 N으로 치환
    dartResult = dartResult.replace("10", "N")
    for char in dartResult:
        #점수 여부 확인
        if char.isdigit():
            point.append(int(char))
        elif char == "N":
            point.append(10)
        #보너스 여부 확인
        elif char in bonus_box:
            point[-1] **= bonus_box[char]
        #옵션 확인 
        elif char == "*":
            if len(point) > 1:
                point[-2] *= 2
            point[-1] *= 2
        elif char == "#":
            point[-1] = -point[-1]
    return sum(point)