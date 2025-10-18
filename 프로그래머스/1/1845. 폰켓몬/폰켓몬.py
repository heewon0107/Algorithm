def solution(nums):
    total = len(nums)
    pick = total // 2
    has = set(nums)
    has_len = len(has)
    
    if pick > has_len:
        return has_len
    else:
        return pick