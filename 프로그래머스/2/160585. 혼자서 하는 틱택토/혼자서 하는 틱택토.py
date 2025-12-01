from collections import deque


def solution(board):
    def is_win(c):
        # 일자 검사
        for i in range(3):
            if all(board[i][j] == c for j in range(3)):
                return True
            if all(board[j][i] == c for j in range(3)):
                return True
            
        # 대각 검사
        if all(board[i][i] == c for i in range(3)):
            return True
        if all(board[i][2-i] == c for i in range(3)):
            return True
        
        return False
    
    # 개수 검사
    o = sum(board[i].count('O') for i in range(3))
    x = sum(board[i].count('X') for i in range(3))
    if not (x <= o <= x+1):
        return 0
    
    o_win = is_win('O')
    x_win = is_win('X')
    if o_win and x_win:
        return 0
        
    if o_win and o-x != 1:
        return 0
    
    if x_win and o != x:
        return 0

    return 1