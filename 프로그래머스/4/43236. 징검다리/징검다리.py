def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    
    left = 0
    right = distance
    while left <= right:
        mid = (left + right) // 2
        
        removed = 0
        prev = 0
        for r in rocks:
            if r - prev < mid:
                removed += 1
            else:
                prev = r
        
        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid -1
            
    return answer