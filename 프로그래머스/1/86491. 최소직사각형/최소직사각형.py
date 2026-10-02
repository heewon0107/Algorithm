def solution(sizes):
    answer = 0
    first = 0
    second = 0
    
    for w, h in sizes:
        big = max(w, h)
        small = min(w, h)
        first = max(first, big)
        second = max(second, small)
    
    answer = first * second
        
    return answer