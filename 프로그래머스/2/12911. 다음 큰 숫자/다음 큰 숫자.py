def solution(n):
    binary = bin(n)
    target = binary.count("1")
    next_num = n + 1
    while target != bin(next_num).count("1"):
        next_num += 1
    return next_num