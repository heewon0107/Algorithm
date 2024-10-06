def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n and field[r][c] != "T"


def dfs(r, c, play):
    # 상우하좌 델타 체크
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
    d = 0

    command = list(map(str, input().split()))
    for go in range(int(command[0])):
        x = command[1][go]
        if x == "A":
            nr = r + delta[d][0]
            nc = c + delta[d][1]
            if is_valid(nr, nc):
                r, c = nr, nc

        elif x == "R":
            d = d + 1 if d < 3 else 0
        elif x == "L":
            d = d - 1 if d > 0 else 3

    if field[r][c] == "Y":
        result[play] = 1


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    field = [input() for _ in range(n)]
    # 시작점 찾고 dfs 실행
    start_check = 0
    for i in range(n):
        if start_check != 0:  # 시작지점 찾았으면 break
            break
        for j in range(n):
            # 시작점이면
            if field[i][j] == "X":
                start_check = (i, j)  # 시작지점 체크
                break
    Q = int(input())
    result = [0] * Q
    for play in range(Q):
        dfs(start_check[0], start_check[1], play)

    print(f"#{tc}", *result)