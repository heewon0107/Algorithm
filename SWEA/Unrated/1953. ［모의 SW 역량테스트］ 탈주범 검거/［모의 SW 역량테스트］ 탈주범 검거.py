# 내가 가능 방향이 연결 가능한가
can_connect = {(-1, 0): (1, 2, 5, 6),  # 상 : 아래 연결 가능
               (0, 1): (1, 3, 6, 7),  # 우 : 좌 연결 가능
               (1, 0): (1, 2, 4, 7),  # 하 : 상 연결 가능
               (0, -1): (1, 3, 4, 5)  # 좌 : 우 연결 가능
               }
# 내 터널 구조가 갈 수 있는 방향
can_direct = {1: (0, 1, 2, 3),
              2: (0, 1),
              3: (2, 3),
              4: (0, 3),
              5: (1, 3),
              6: (1, 2),
              7: (0, 2)
              }

delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상 하 좌 우


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < M


def search(r, c, time):
    global result
    if time == L:
        return

    direction = can_direct[tunnel[r][c]]
    for d in direction:
        dr, dc = delta[d]
        nr = r + dr
        nc = c + dc
        if is_valid(nr, nc) and not visited[nr][nc] and tunnel[nr][nc] in can_connect[(dr, dc)]:
            visited[nr][nc] = 1
            escape[nr][nc] = 1
            search(nr, nc, time + 1)
            visited[nr][nc] = 0


T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    escape = [[0] * M for _ in range(N)]
    escape[R][C] = 1
    search(R, C, 1)
    for i in range(N):
        for j in range(M):
            if escape[i][j]:
                result += 1
    print(f"#{tc} {result}")