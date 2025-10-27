def solution(diffs, times, limit):
    n = len(diffs)
    
    l = 1
    r = max(diffs)
    answer = max(diffs)
    
    while l < r:
        mid = (l + r) // 2
        time = times[0]
        
        for i in range(1,n):
            diff = 0
            if mid < diffs[i]:
                diff = diffs[i] - mid
            
            time += diff*(times[i] + times[i-1]) + times[i]
        
        if time <= limit:
            answer = mid
            r = mid
        else:
            l = mid + 1
            
            
    return answer