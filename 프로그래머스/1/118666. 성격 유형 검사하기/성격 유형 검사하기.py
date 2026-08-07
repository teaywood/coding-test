def solution(survey, choices):
    score = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    comp_type = ["RT", "CF", "JM", "AN"]
    result = []
    
    for surv, cho in zip(survey, choices):
        if cho == 4:
            continue
        if 1 <= cho < 4:
            score[surv[0]] += 4 - cho
        else:
            score[surv[1]] += cho - 4
            
    for typebox in comp_type:
        left = score[typebox[0]]
        right = score[typebox[1]]
        if left > right:
            result.append(typebox[0])
        elif left < right:
            result.append(typebox[1])
        else:
            result.append(typebox[0])
    
    return "".join(result)

