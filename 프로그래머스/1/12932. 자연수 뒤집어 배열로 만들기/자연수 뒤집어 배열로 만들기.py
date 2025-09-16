def solution(n):
    lst = list(str(n))
    lst = list(map(int, lst))
    
    return lst[::-1]