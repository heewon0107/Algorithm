from collections import deque

global N, L, R
def bfs(r, c):
    q = deque([(r,c)])
    team = [(r,c, world[r][c])]
    while q:
        r, c = q.popleft()
        
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(world[nr][nc] - world[r][c]) <= R:
                visited[nr][nc] = 1
                team.append((nr,nc,world[nr][nc]))
                q.append((nr,nc))
        
    return team

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
N, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(N)]
result = 0
# 1. 이동 가능할 때까지 이동
can_move = True
while can_move:
    can_move = False
    visited = [[0] * N for _ in range(N)]

    # 2. 한 나라에서 이동가능한 연합 구하기
    teams = deque() # 연합리스트
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                team = bfs(i,j)
                if len(team) > 1:
                    teams.append(team)
                    can_move = True

    # 3. 이동
    while teams:
        team = teams.popleft()
        total = 0
        for x,y, t in team:
            total += t
        total /= len(team)
        total = int(total)
        for r, c, p in team:
            world[r][c] = total
    # 1번이라도 이동했다면 +1
    if can_move:
        result += 1
print(result)