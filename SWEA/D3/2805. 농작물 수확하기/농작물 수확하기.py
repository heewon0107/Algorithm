t = int(input())
for tc in range(1, t + 1):
    n = int(input())    # 농작물 크기.
    farm = [input() for _ in range(n)]
    result = 0
    mid = n // 2
    for i in range(n):
        for j in range(n):
            a = mid - abs(n // 2 - i)
            if mid - a <= j <= mid + a:
                result += int(farm[i][j])
    print(f"#{tc} {result}")