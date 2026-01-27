def solution(n, cores):
    # 이미 끝남
    if n <= len(cores):
        return n
    
    # 시간의 작업량 함수
    def work_cnt(t):
        return sum(t // c for c in cores) + len(cores)
    
    # r = 최대 소요 시간
    l, r = 0, max(cores) * n
    
    while l < r:
        mid = (l + r) // 2
        
        # 작업량이 많으면 시간 줄이기
        if n <= work_cnt(mid):
            r = mid
        # 적으면 시간 늘리기
        else:
            l = mid + 1
    
    # 총 시간
    time = l
    
    # 이전까지 작업량
    done = work_cnt(time-1)
    
    for i, c in enumerate(cores):
        if time % c == 0: # 작업가능 한 코어
            done += 1
            if n == done: # 마지막 작업이다.
                return i + 1
    return 0