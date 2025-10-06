def solution(elements):
    n = len(elements)
    dummy = set()
    
    for i in range(n):
        s = 0
        for j in range(n):
            s += elements[(i+j) % n]
            dummy.add(s)
    
    return len(dummy)