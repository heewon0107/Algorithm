def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = n - 1
    
    while d >= 0 or p >= 0:
        
        while d >= 0 and not deliveries[d]:
            d -= 1
        
        while p >= 0 and not pickups[p]:
            p -= 1
        
        if d < 0 and p < 0:
            break
            
        distance = max(d, p)
        answer += (distance + 1) * 2
        
        remain = cap
        i = d
        while i >= 0 and remain > 0:
            if deliveries[i] > remain:
                deliveries[i] -= remain
                remain = 0
            else:
                remain -= deliveries[i]
                i -= 1
        d = i
        
        remain = cap
        j = p
        while j >= 0 and remain > 0:
            if pickups[j] > remain:
                pickups[j] -= remain
                break
            else:
                remain -= pickups[j]
                j -= 1
        p = j
        
    return answer