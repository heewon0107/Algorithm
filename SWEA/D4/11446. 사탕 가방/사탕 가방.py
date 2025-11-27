for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    candies = list(map(int, input().split()))
    
    left = 1
    right = max(candies)
    result = 0
    
    while left <= right:
        mid = (left+right) // 2
        
        cnt = 0
        for c in candies:
            cnt += c // mid
        
        if cnt >= M:
            result = mid
            left = mid + 1
        else:
            right = mid -1
    print(f'#{tc} {result}')