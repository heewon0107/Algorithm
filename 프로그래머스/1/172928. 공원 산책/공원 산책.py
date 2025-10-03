def solution(park, routes):
    answer = []
    
    H = len(park) # 3 <= H <= 50
    W = len(park[0]) # 3 <= W <= 50
    pos = (0, 0)
    s = False
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                pos = (i,j)
                s = True
                break
        if s:
            break
    
    # for Command
    for route in routes: # O(50)
        d, x = route.split(" ")
        x = int(x) # 1 <= x <= 9
        ni, nj = pos
        can_go = True
        if d == 'N':
            for i in range(1, x + 1):
                ni = pos[0] - i
                if ni >= H or ni < 0:
                    can_go = False
                    break
                if park[ni][nj] == 'X':
                    can_go = False
                    break
        elif d == 'E':
            for i in range(1, x + 1):
                nj = pos[1] + i
                if nj >= W or nj < 0:
                    can_go = False
                    break
                if park[ni][nj] == 'X':
                    can_go = False
                    break
        elif d == 'S':
            for i in range(1, x + 1):
                ni = pos[0] + i
                if ni >= H or ni < 0:
                    can_go = False
                    break
                if park[ni][nj] == 'X':
                    can_go = False
                    break
        elif d == 'W':
            for i in range(1, x + 1):
                nj = pos[1] - i
                if nj >= W or nj < 0:
                    can_go = False
                    break
                if park[ni][nj] == 'X':
                    can_go = False
                    break
          
        if can_go:
            pos = ni, nj
            # if 범위? continue
            # if 장애물? continue
    
    
    return list(pos)