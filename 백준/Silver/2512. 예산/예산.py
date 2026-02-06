def solution():

    N = int(input())
    requests = list(map(int, input().split()))
    budget = int(input())

    # Binary Search
    l = 0
    r = max(requests)
    result = 1

    # O(log100000)
    while l <= r:
        # Mid is a Maximum price
        mid = (l + r) // 2

        total = 0
        # O(10000)
        for request in requests:
            if request >= mid:
                total += mid
            else:
                total += request
        
        if total == budget:
            return mid
        elif total < budget:
            result = mid
            l = mid + 1
        elif total > budget:
            r = mid - 1
    
    return result

print(solution())