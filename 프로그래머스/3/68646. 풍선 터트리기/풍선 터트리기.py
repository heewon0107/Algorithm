def solution(a):
    answer = 2
    n = len(a)
    dp_l = [a[0]] + [0] * (n - 1)
    dp_r = [0] * (n-1) + [a[-1]]
    
    for i in range(1, n):
        dp_l[i] = min(a[i], dp_l[i-1])
        
    for i in range(n-2, -1, -1):
        dp_r[i] = min(a[i], dp_r[i+1])
    
    for i in range(1, n-1):
        if dp_l[i-1] > a[i] or dp_r[i+1] > a[i]:
            answer += 1
    return answer