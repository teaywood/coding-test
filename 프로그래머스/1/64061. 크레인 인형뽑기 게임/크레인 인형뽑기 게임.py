def solution(board, moves):
    board_aranged = [[doll for doll in line if doll]for line in list(zip(*board))]
    box = []
    count = 0
    for pick_line in moves:
        if board_aranged[pick_line-1]:
            doll = board_aranged[pick_line-1].pop(0)
            if box and doll == box[-1]:
                del box[-1]
                count += 2
            else:
                box.append(doll)
    return count