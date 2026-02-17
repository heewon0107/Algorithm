from collections import deque

def solution(n, m, board):
    answer = 0
    delta = [(0,1), (1,0), (1,1)]   # 우,하,우하
    board = [list(b) for b in board]
    
    def two_two(r, c):
        lst = [(r, c)]
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            # 다른 블럭
            if board[r][c] != board[nr][nc]:
                return False
            else:
                lst.append((nr, nc))
        return lst
    
    def reset(i, j):
        o_list = deque()
        while i >= 0:
            block = board[i][j]
            if block == -1:
                break
            
            elif block == 0:
                o_list.append(i)
                
            else:
                # 떨어질 곳이 있다.
                if o_list:  
                    board[o_list.popleft()][j] = block
                    board[i][j] = 0
                    o_list.append(i)
            i -= 1
        
        while o_list:
            board[o_list.popleft()][j] = -1
        
        
    while True:
        blocks = set()

        # 2x2 검사 O(900*3)
        for i in range(n-1):
            for j in range(m-1):
                # 빈 공간
                if board[i][j] == -1 or board[i][j] == 0:
                    continue
                # 검사
                block = two_two(i, j)
                if block:
                    blocks.update(block)
                    
        # 격파 할 블록 없으면 return
        if not blocks:
            break
        
        # 블록 격파
        for i, j in blocks:
            board[i][j] = 0
            answer += 1
            
        # 보드 리셋 O(900)
        for j in range(m):
            reset(n - 1, j)
    
    return answer