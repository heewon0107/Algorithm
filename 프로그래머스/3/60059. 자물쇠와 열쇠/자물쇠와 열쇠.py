def rotate(arr):
    return list(zip(*arr[::-1]))

def solve(r,c,key,board,N,M):
    can_solve = True
    
    for i in range(M):
        for j in range(M):
            board[i+r][j+c] += key[i][j]
    
    for i in range(N):
        if not can_solve:
            break
        
        for j in range(N):
            if board[i+M][j+M] != 1:
                can_solve = False
                break
            
    for i in range(M):
        for j in range(M):
            board[i+r][j+c] -= key[i][j]
    
    return can_solve
    
def solution(key, lock):
    N, M = len(lock), len(key)
    
    board = [[0] * (N + 2*M) for _ in range(N + 2*M)]
    for i in range(N):
        for j in range(N):
            board[i+M][j+M] = lock[i][j]
            
    for i in range(4):
        key = rotate(key)
        
        for r in range(1, N+M):
            for c in range(1, N+M):
                if solve(r,c,key,board,N,M):
                    return True
                
    
    return False