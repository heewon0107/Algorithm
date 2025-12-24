def solution(n):
    snail = [[0] * (i + 1) for i in range(n)]
    
    num = 1
    r, c = -1, 0
    # 하, 우, 좌 대각
    delta = [(1, 0), (0, 1), (-1, -1)]
    d = 0
    
    for length in range(n, 0, -1):
        dr, dc = delta[d]
        for _ in range(length):
            r += dr
            c += dc
            snail[r][c] = num
            num += 1
        d = (d+1) % 3
        
    answer = []
    for a in snail:
        answer += a
    # return [x for row in snail]
    return answer