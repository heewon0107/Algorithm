def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m

# 상 우 하 좌
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

# for tc in range(1, t + 1):
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
q = []
for i in range(n):
    for j in range(m):
        if board[i][j] > 0:
            q.append((i, j))

while q:
    # 다음날에 익을게
    yesterday_q = q
    q = []
    while yesterday_q:
        r, c = yesterday_q.pop()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            # 익지 않은 토마토 익히기.
            if is_valid(nr, nc) and not board[nr][nc]:
                board[nr][nc] = 1
                q.append((nr, nc))
    result += 1
    # 다음날 봐야되면 1일 추가.
# 상자 검사하며 안 익은 토마토 찾기.
if result > 0:
    result -= 1
for i in range(n):
    if result == -1:
        break
    for j in range(m):
        if not board[i][j]:
            result = -1
            break
print(result)