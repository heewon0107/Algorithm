def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        blank = 0
        mid = (left + right) // 2
        
        for stone in stones:
            if stone - mid <= 0: 
                blank += 1
            else:
                blank = 0
            if blank >= k:
                break
        
        if k <= blank:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
                
    return answer