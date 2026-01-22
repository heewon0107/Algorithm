def solution(n):
    n = str(n)
    
    return int(''.join(sorted(n, reverse=True)))