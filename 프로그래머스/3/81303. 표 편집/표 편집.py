def solution(n, k, cmd):
    prev = [i - 1 for i in range(n)]
    next_ = [i + 1 for i in range(n)]
    next_[-1] = -1
    
    stack = []
    for c in cmd:
        # UP
        if c[0] == 'U':
            for _ in range(int(c[2:])):
                k = prev[k]
        # DOWN
        elif c[0] == 'D':
            for _ in range(int(c[2:])):
                k = next_[k]
        # CLEAR
        elif c[0] == 'C':
            stack.append(k)
            
            # 이전 길 변경
            if prev[k] != -1:
                next_[prev[k]] = next_[k]
            
            # 다음 길 변경
            if next_[k] != -1:
                prev[next_[k]] = prev[k]
            
            # 삭제 후 다음 행
            if next_[k] != -1:
                k = next_[k]
            # 다음 행 없으면 이전 행
            else:
                k = prev[k]
        
        # Z
        elif c[0] == 'Z':
            r = stack.pop()
            if prev[r] != -1:
                next_[prev[r]] = r
            if next_[r] != -1:
                prev[next_[r]] = r
        
    answer = ['O'] * n
    for x in stack:
        answer[x] = 'X'
    
    return ''.join(answer)