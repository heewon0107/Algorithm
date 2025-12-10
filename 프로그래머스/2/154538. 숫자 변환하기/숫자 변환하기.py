from collections import deque

def solution(x, y, n):
    visited = set()
    q = deque([(x, 0)])
    visited.add(x)
    
    while q:
        x, cnt = q.popleft()
        if x == y:
            return cnt
        
        for nx in [x+n, x*2, x*3]:
            if nx <= y and nx not in visited:
                visited.add(nx)
                q.append((nx, cnt + 1))
                
    
    return -1