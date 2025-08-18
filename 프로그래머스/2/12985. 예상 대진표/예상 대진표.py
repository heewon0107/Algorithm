def solution(n,a,b):
    answer = 0

    while a != b:
        answer += 1     # Victory
        a = a // 2 + a % 2    # nextNumber
        b = b // 2 + b % 2

    return answer