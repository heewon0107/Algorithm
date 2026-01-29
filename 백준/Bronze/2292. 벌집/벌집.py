N = int(input())

def solution(n):
    if n == 1:
        return 1
    
    cur = 1
    x = 6
    i = 1
    while cur < n:
        cur += x*i
        i += 1
    return i

print(solution(N))
    