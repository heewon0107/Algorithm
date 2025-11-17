# 상 하 좌 우
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def is_valid(r, c, N):
    return 0 <= r < N and 0 <= c < N

def can_connect(r, c, d, board, N):
    nr = r + dr[d]
    nc = c + dc[d]
    length = 0

    while is_valid(nr, nc, N):
        # 빈 공간이 아닐 경우
        if board[nr][nc]:
            return 0
        
        length += 1
        nr += dr[d]
        nc += dc[d]

    return length

def set_wire(r, c, d, board, N, val):
    """ 전선 연결 함수 val 2(연결) or 0(해제)"""
    nr = r + dr[d]
    nc = c + dc[d]

    while is_valid(nr, nc, N):
        board[nr][nc] = val
        nr += dr[d]
        nc += dc[d]

def dfs(idx, cores, board, N, connect, length, total):
    global max_connect, min_len

    # 가지치기 현재 남은 core를 다 더해도 안 됨
    if connect + (total-idx) < max_connect:
        return
    
    # 도달
    if idx == total:
        if connect > max_connect:
            max_connect = connect
            min_len = length
        elif connect == max_connect:
            min_len = min(min_len, length)
        return
    
    r, c = cores[idx]

    # 4방향 탐색
    for d in range(4):
        dist = can_connect(r, c, d, board, N)
        if dist:
            set_wire(r, c, d, board, N, 2)
            dfs(idx+1, cores, board, N, connect+1, length+dist, total)
            set_wire(r, c, d, board, N, 0)

    # 연결하지 않고 dfs
    dfs(idx+1, cores, board, N, connect, length, total)

for tc in range(1, int(input())+1):
    N =int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_connect = -1
    min_len = 1e9

    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j]:
                cores.append((i, j))

    total = len(cores)
    dfs(0, cores, board, N, 0, 0, total)

    print(f'#{tc} {min_len}')