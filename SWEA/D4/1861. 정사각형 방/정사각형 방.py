from collections import deque


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


def dijkstra(r, c):
    if "기저 조건":
        pass
    first_num = board[r][c]
    cnt = 1
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if is_valid(nr, nc) and board[nr][nc] == board[r][c] + 1:
                q.append((nr, nc))
                cnt += 1
                break

    if cnt > result[1]:
        result[0] = first_num
        result[1] = cnt
    elif cnt == result[1] and first_num < result[0]:
        result[0] = first_num


# 상 우 하 좌
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    result = [1e9, 0]
    for i in range(n):
        for j in range(n):
            dijkstra(i, j)

    print(f"#{tc}", *result)