def solution(sequence, k):
    l = 0
    n = len(sequence)
    cnt = 1e9
    answer = []
    total = 0
    
    for r in range(n):
        total += sequence[r]
        while total > k:
            total -= sequence[l]
            l += 1
        
        if total == k:
            if r-l < cnt:
                cnt = r-l
                answer = [l,r]
        
    return answer