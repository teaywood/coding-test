def solution(data, ext, val_ext, sort_by):
    sort_box = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = []
    for d in data:
        if d[sort_box[ext]] < val_ext:
            answer.append(d)
    return sorted(answer, key=lambda x: x[sort_box[sort_by]])