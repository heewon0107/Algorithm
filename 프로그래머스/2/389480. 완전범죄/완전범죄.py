def solution(info, n, m):
    min_a = 1e9
    visited = set()
    
    def fn(idx, a, b):
        nonlocal min_a
        
        # 가지치기
        if min_a <= a:
            return
        
        # 최대 흔적
        if a >= n or b >= m:
            return
        
        # 보석 다 먹음
        if idx == len(info):
            min_a = min(min_a, a)
            return
        
        state = (idx, a, b)
        if state in visited:
            return
        visited.add(state)
        
        
        fn(idx + 1, a + info[idx][0], b)
        fn(idx + 1, a, b + info[idx][1])

    fn(0, 0, 0)
    
    return min_a if min_a < n else -1