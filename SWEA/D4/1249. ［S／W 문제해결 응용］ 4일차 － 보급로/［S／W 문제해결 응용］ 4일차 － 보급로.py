from collections import deque


def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n


# 상 우 하 좌
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = list(input() for _ in range(n))
    dijkstra = [[1e9] * n for _ in range(n)]
    dijkstra[0][0] = 0
    q = deque()
    q.append((0, 0))

    while q:
        r, c = q.popleft()

        if r == n - 1 and c == n - 1:
            if q:
                q.popleft()
            else:
                break

        cur_distance = dijkstra[r][c]
        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            if is_valid(nr, nc):
                distance = int(board[nr][nc]) + cur_distance  # 누적 거리
                if distance < dijkstra[nr][nc]:
                    dijkstra[nr][nc] = distance
                    q.append((nr, nc))

    print(f"#{tc}", dijkstra[n-1][n-1])