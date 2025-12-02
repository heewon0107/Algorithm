from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)]
    
    def mass(i, j):
        # 석유의 양
        quantity = 0
        
        # 업데이트할 목록
        lst = []       
        
        # BFS
        q = deque([(i, j)])
        while q:
            quantity += 1
            r, c = q.popleft()
            lst.append((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and land[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                    
        return (quantity, lst)
    
    # O(250000)
    id = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                visited[i][j] = 1
                v, lst = mass(i, j)
                for r, c in lst:
                    land[r][c] = (v, id)
                id += 1
                    
    row = col = 0
    result = 0
    cur = 0
    visited = set()
    while col < m:
        # 석유 있다.
        if land[row][col] and land[row][col][1] not in visited:
            cur += land[row][col][0]
            visited.add(land[row][col][1])
            
            # 해당 석유 덩어리 Pass
            while row < n and land[row][col]:
                row += 1
                
        # 석유 없다. (다음 칸 시추)
        else:
            row += 1
        
        # 땅 끝이다.
        if row == n:
            result = max(result, cur)
            cur = 0
            row = 0
            col += 1
            visited.clear()
            
    return result