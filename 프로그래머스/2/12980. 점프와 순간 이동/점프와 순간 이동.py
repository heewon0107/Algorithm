def solution(n):
    
    # 시간초과 O(10억)
    # battery = [0] * (n+1)
    # battery[1] = 1
    # for i in range(2, n+1):
    #     # 순간이동 불가
    #     if i % 2:
    #         battery[i] = battery[i-1] + 1
    #     # 순간이동 가능
    #     else:
    #         battery[i] = battery[int(i / 2)]
    # return battery[n] % 1234567
    bat = 0
    while n > 0:
        if n % 2:
            n -= 1
            bat += 1
        else:
            n //= 2
    return bat
            