T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    result = 0
    while B >= C:
        B -= 1
        result += 1
    while A >= B:
        A -= 1
        result += 1
    if C < 3 or A < 1 or B < 1:
        result = -1
    print(f"#{tc} {result}")
