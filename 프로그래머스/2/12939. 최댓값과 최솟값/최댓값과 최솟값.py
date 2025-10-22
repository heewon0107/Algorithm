def solution(s):
    lst = list(map(int, s.split(' ')))
    lst.sort()
    return f'{lst[0]} {lst[-1]}'