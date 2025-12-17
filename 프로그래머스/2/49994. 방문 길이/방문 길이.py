def solution(dirs):
    command = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }
    answer = set()
    r = c = 0
    for d in dirs:
        dr, dc = command[d]
        nr = r + dr
        nc = c + dc
        if abs(nr) > 5 or abs(nc) > 5:
            continue
        answer.add((max(r,nr), max(c,nc), min(r, nr), min(c, nc)))
        r = nr
        c = nc
        
    return len(answer)