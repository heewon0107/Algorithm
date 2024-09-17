import math


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    i = int(math.sqrt(N))
    while 1:
        if N % i == 0:
            break
        else:
            i -= 1
    j = N // i
    result = i + j - 2
    print(f"#{tc} {result}")