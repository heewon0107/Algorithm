from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    visited = [[0] * m for _ in range(n)]
    r = 0
    c = 0
    for i in range(n):
        b = board[i]
        x = b.find('R')
        if x > 0:
            r = i
            c = x
            break
    
    visited[r][c] = 1
    q = deque([(r,c,0)])
    while q:
        r, c, cnt = q.popleft()
        
        if board[r][c] == 'G':
            return cnt
        
        # 4분면 돌며 한 칸 이상 갈 수 있나 체크
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr = r + dr
            nc = c + dc
            
            # 진행 가능한가?
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 'D':
                # 벽까지 진행
                while 0 <= nr < n and 0 <= nc < m and board[nr][nc] != 'D':
                    nr += dr
                    nc += dc
                nr -= dr
                nc -= dc
                
                # 첫 방문
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr,nc,cnt+1))
        
    return -1