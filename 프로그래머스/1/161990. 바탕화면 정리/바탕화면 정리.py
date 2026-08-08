def solution(wallpaper):
    coords = [(x, y) for x, row in enumerate(wallpaper) for y, cell in enumerate(row) if cell == '#']
    
    rows = [x for x, y in coords]
    cols = [y for x, y in coords]
    
    lux, luy = min(rows), min(cols)
    rdx, rdy = max(rows)+1, max(cols)+1
    
    return [lux, luy, rdx, rdy]