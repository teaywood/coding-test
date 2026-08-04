from collections import Counter

def solution(X, Y):
    X_counter = Counter(X)
    Y_counter = Counter(Y)
    num_box = []
    for i in range(9, -1, -1):
        i = str(i)
        for _ in range(min(X_counter[i], Y_counter[i])):
            num_box.append(i)
    
    if not num_box:
        return "-1"
    if list(set(num_box)) == ["0"]:
        return "0"
    return ''.join(num_box)