def solution(maps):
    from collections import deque
    
    def bfs(r, c):
        nonlocal N, M
        total = 0
        q = deque([(r, c)])
        
        while q:
            r, c = q.popleft()
            total += int(maps[r][c])
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc] != 'X':
                    q.append((nr, nc))
                    visited[nr][nc] = 1
        return total    
        
    answer = []
    N, M = len(maps), len(maps[0])
    visited = [[0] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and maps[i][j] != 'X':
                visited[i][j] = 1
                answer.append(bfs(i, j))
    
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer