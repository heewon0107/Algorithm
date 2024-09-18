T = int(input())
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    r = c = 0
    d = 0
    x = 1
    while x <= N ** 2:
        arr[r][c] = x
        x += 1

        dr, dc = delta[d]
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            if d < 3:
                d += 1
            else:
                d = 0
            dr, dc = delta[d]
            r = r + dr
            c = c + dc
    print(f"#{tc}")
    for i in arr:
        print(*i)