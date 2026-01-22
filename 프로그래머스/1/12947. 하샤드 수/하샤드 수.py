def solution(x):
    n = 0
    for i in str(x):
        n += int(i)
    if x % n:
        return False
    else:
        return True