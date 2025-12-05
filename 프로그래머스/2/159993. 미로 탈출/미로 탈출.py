def solution(maps):
    from collections import deque
    
    delta = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def bfs(r, c, N, M, target):
        q = deque([(r,c, 0)])
        visited = [[False] * M for _ in range(N)]
        visited[r][c] = True
        
        while q:
            r, c, cnt = q.popleft()
            if maps[r][c] == target:
                return cnt
            
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not maps[nr][nc] == 'X':
                    visited[nr][nc] = True
                    q.append((nr,nc,cnt+1))
                    
        return -1
    
    N, M = len(maps), len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'L':
                lever = bfs(i, j, N, M, 'S')
                if lever == -1: return -1   
                
                exit = bfs(i, j, N, M, 'E')
                if exit == -1:  return -1
            
                return lever + exit
        
