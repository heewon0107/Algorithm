def solution(priorities, location):
    
    from collections import deque
    
    q = deque([(i,p) for i, p in enumerate(priorities)])
    
    cnt = 0
    while q:
        i, p = q.popleft()
        if q:
            max_p = max(q, key=lambda x: x[1])[1]
        else:
            max_p = 0
            
        if p < max_p:
            q.append((i, p))
            continue
        else:
            cnt += 1
            
        if i == location:
            return cnt
