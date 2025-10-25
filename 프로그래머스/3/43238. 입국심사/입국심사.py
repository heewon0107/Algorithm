def solution(n, times):
    # 심사 최대/최소 시간
    times.sort()
    left = 0
    right = times[-1] * n
    
    answer = 0
    while left <= right:
        mid = (left+right) // 2
        
        people = 0
        for i in range(len(times)):
            people += mid // times[i]
        
        if people < n:
            left = mid + 1
        else: # 모두 심사 완료
            right = mid - 1
            answer = mid
        
    return answer