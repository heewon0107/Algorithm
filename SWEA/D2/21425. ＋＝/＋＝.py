T = int(input())
for tc in range(1, T + 1):
    a, b, n = map(int, input().split())
    cnt = 0
    if a > b:
        a, b = b, a
    # 둘 다 n 보다 작다.
    while a <= n and b <= n:
        cnt += 1
        a += b
        if a > n:
            break
        b += a
        cnt += 1

    print(cnt)