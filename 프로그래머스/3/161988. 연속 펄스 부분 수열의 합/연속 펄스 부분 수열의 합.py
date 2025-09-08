def solution(sequence):
    dp1 = [value if i % 2 == 0 else -value for i, value in enumerate(sequence)]
    dp2 = list(map(lambda x: -x, dp1))
    
    for i in range(1, len(dp1)):
        dp1[i] = max(dp1[i], dp1[i-1] + dp1[i])
        dp2[i] = max(dp2[i], dp2[i-1] + dp2[i])
        
    answer = max(max(dp1), max(dp2))
    return answer