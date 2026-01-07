def solution(n):
    answer = 0
    board = [[0] * n for _ in range(n)]
    
    def dfs(i):
        nonlocal answer, n
        # n개의 퀸 배치 완료
        if i == n:
            answer += 1
            return
        
        # n개의 col 검사 후 갱신
        for j in range(n):
            if check(i, j):
                board[i][j] = 1
                dfs(i+1)
                board[i][j] = 0
    
    # 배치 가능 여부 검사
    def check(r, c):
        nonlocal n
        # 직선 검사
        nr = r
        while nr > 0:
            nr -= 1
            # 퀸 있으면 False
            if board[nr][c]:
                return False
        
        # 좌상 검사
        nr, nc = r, c
        while nr > 0 and nc > 0:
            nr -= 1
            nc -= 1
            if board[nr][nc]:
                return False
        
        # 우상 검사
        nr, nc = r, c
        while nr > 0 and nc < n-1:
            nr -= 1
            nc += 1
            if board[nr][nc]:
                return False
        
        return True
    
    dfs(0)
    return answer