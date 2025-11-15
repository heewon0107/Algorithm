from collections import deque
delta = [(1,-1), (1,0), (1,1), (-1,-1), (-1,0), (-1,1), (0,-1), (0,1)]

def bomb(n, i,j):
    cnt = 0
    for di, dj in delta:
        ni, nj = i+di, j+dj
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == '*':
            cnt += 1
    return cnt

def explode(n,i,j):
    q = deque([(i,j)])

    while q:
        r, c = q.popleft()

        # 연쇄 폭팔
        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = 1
                # 주변에 지뢰 없는 곳인 경우
                if not board[nr][nc]:
                    q.append((nr,nc))


for tc in range(1, int(input())+1):
    result = 0
    N = int(input())
    board = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 지뢰면 미리 체크
            if board[i][j] == '*':
                visited[i][j] = 1
            # 공간이면 지뢰 찾기
            else:
                board[i][j] = bomb(N,i,j)

    for i in range(N):
        for j in range(N):
            # 주변 지뢰가 0임
            if not visited[i][j] and not board[i][j]:
                visited[i][j] = 1
                explode(N,i,j)
                result += 1


    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result += 1

    print(f'#{tc} {result}')