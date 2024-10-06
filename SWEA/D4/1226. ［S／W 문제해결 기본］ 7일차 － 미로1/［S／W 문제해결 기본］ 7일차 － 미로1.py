def is_valid(r, c):
    return maze[r][c] == "0" or maze[r][c] == "3"


def dfs(r, c):
    global result
    if result == 1:  # 갈 길 이미 찾았다.
        return
    if maze[r][c] == "3":
        result = 1
        return

    visited[r][c] = 1   # 방문 체크
    # 상우하좌 델타 체크
    for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        nr = r + dr
        nc = c + dc
        if is_valid(nr, nc) and not visited[nr][nc]:
            dfs(nr, nc)

t = 10
for tc in range(1, 10 + 1):
    num = input()
    maze = [input() for _ in range(16)]
    result = 0
    visited = [[0] * 16 for _ in range(16)]
    # 시작점 찾고 dfs 실행
    start_check = 0
    for i in range(1, 15):
        if start_check == 1:  # 시작지점 찾았으면 break
            break
        for j in range(1, 15):
            # 시작점이면
            if maze[i][j] == "2":
                dfs(i, j)
                start_check = 1  # 시작지점 체크
                break

    print(f"#{tc} {result}")