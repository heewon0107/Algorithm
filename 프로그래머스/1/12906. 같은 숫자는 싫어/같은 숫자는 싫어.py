def solution(arr):
    result = []
    for num in arr:
        if not result:
            result.append(num)
            continue
            
        if num != result[-1]:
            result.append(num)
    return result