def solution(maps):
    from collections import deque
    
    def bfs():
        nonlocal N, M
        
        q = deque([])
        q.append((0,0,1))
        visited[0][0] = 1
        while q:
            r, c, total = q.popleft()
            if r == N - 1 and c == M - 1:
                return total
            
            for dr, dc in [(0,1), (1,0), (0,-1), (-1, 0)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr,nc,total+1))
    
        return -1
    
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    answer = bfs()
    
    return answer