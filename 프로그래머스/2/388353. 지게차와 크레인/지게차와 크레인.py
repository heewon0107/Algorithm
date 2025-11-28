def solution(storage, requests):
    delta = [(-1,0), (1,0), (0,1), (0,-1)]
    from collections import deque
    
    # 근처 여는 함수
    def near(i, j, delta):
        is_outside = False
        
        for dr, dc in delta:
            nr = dr + i
            nc = dc + j
            if storage[nr][nc] == '0':
                storage[i][j] = '0'
                is_outside = True
                break
        
        if is_outside:
            for dr, dc in delta:
                nr, nc = dr+i, dc+j
                if storage[nr][nc] == '1':
                    storage[nr][nc] = '0'
                    near(nr,nc,delta)
    
    N = len(storage)
    M = len(storage[0])
    storage = [list('0' + lst + '0') for lst in storage]
    storage.insert(0, list('0' * (M+2)))
    storage.append(list('0' * (M+2)))
    
    containers = deque()
    for r in requests:
        # 지게차
        if len(r) == 1:
            for i in range(1, N+1):
                for j in range(1, M+1):
                    if storage[i][j] == r:
                        for dr, dc in delta:
                            nr = dr + i
                            nc = dc + j
                            if storage[nr][nc] == '0':
                                containers.append((i,j))
                                break
                              
            while containers:
                r, c = containers.popleft()
                storage[r][c] = '0'
                near(r,c, delta)
            
        # 크레인
        else:
            for i in range(1, N+1):
                for j in range(1, M+1):
                    if storage[i][j] == r[0]:
                        storage[i][j] = '1'
                        near(i, j, delta)
    result = 0                        
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not storage[i][j].isdigit():
                result += 1
            
    return result