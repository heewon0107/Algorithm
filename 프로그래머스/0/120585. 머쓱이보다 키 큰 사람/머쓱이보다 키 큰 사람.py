def solution(array, height):
    cnt = 0
    for a in array:
        if height < a:
            cnt += 1
    return cnt