def solution(price, money, count):
    total = 0
    cnt = 1
    for _ in range(count):
        total += price * cnt
        cnt += 1
            
    return total - money if money <= total else 0