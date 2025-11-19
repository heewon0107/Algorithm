# 우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def dfs(x, y, r, c, d, N, cnt):
    global result

    # 다음 위치 결정
    nr = r + dr[d]
    nc = c + dc[d]
    
    # 엔드포인트 result 갱신
    if nr == x and nc == y and d == 3:
        result = max(result, cnt)
        return
    
    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and board[nr][nc] not in eaten:
        visited[nr][nc] = True
        eaten.add(board[nr][nc])
        dfs(x, y, nr, nc, d, N, cnt+1)
        visited[nr][nc] = False
        eaten.remove(board[nr][nc])

    if r == x and y == c:
        return
    
    if d < 3:
        dfs(x, y, r, c, d+1, N, cnt)
    
        
for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    visited = [[False] * N for _ in range(N)]
    eaten = set()
    
    for i in range(N-1):
        if (N-i) * 2 - 2 <= result:
            break
        for j in range(1, N-1):
            eaten.add(board[i][j])
            visited[i][j] = True
            dfs(i, j , i, j, 0, N, 1)
            visited[i][j] = False
            eaten.remove(board[i][j])

    print(f'#{tc} {result}')
