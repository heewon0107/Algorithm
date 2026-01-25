from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 2배
    rectangle = [[x*2, y*2, X*2, Y*2] for x, y, X, Y in rectangle]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    MAX = 102
    board = [[0]*MAX for _ in range(MAX)]

    # 1. 사각형 영역 채우기
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                board[y][x] = 1

    # 2. 내부 제거 (테두리만 남김)
    for x1, y1, x2, y2 in rectangle:
        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                board[y][x] = 0

    # 3. BFS
    q = deque([(characterY, characterX, 0)])
    visited = [[0]*MAX for _ in range(MAX)]
    visited[characterY][characterX] = 1

    while q:
        y, x, d = q.popleft()
        if y == itemY and x == itemX:
            return d // 2

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = y+dy, x+dx
            if board[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append((ny, nx, d+1))
