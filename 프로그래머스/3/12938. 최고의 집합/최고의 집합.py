def solution(n, s):
    if n > s:
        return [-1]
    default = s // n
    arr = [default] * n
    others = s % n
    idx = -1
    while others:
        arr[idx] += 1
        idx -= 1
        others -= 1
        
    
    return arr