def solution(arr):
    min_val = min(arr)
    arr.remove(min_val)
    return arr if arr else [-1]