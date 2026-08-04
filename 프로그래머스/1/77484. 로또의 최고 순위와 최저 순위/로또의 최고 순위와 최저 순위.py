def solution(lottos, win_nums):
    
    def cal_rate(mat):
        match mat:
            case 6:
                return 1
            case 5:
                return 2
            case 4:
                return 3
            case 3:
                return 4
            case 2:
                return 5
            case _:
                return 6

    num = lottos.count(0)
    matching_count = len(set(lottos) & set(win_nums))
    return [cal_rate(matching_count+num), cal_rate(matching_count)]