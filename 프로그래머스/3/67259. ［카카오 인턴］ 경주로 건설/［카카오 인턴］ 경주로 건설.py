def solution(board):
    def dfs(r, c, price, visited, direction):
        
        
        if price > min_cost[r][c]:
            return
        else:
            min_cost[r][c] = price
        
        if r == n-1 and c == n-1:
            return
        
        for dr, dc, d in [(0,1,"r"), (1,0,"d"), (0,-1,"l"), (-1,0,"u")]:
            nr = r + dr
            nc = c + dc
            
            # vaild and visited check:
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc] and not visited[nr][nc]:
                cost = 100 if direction == d else 600
                           
                visited[nr][nc] = True
                dfs(nr, nc, price + cost, visited, d)
                visited[nr][nc] = False
        
    n = len(board[0])
    min_cost = [[1e9] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    
    answer = 0
    
    for d in ["r", "d"]:
        dfs(0,0,0,visited, d)        
            
    
    return min_cost[n-1][n-1]