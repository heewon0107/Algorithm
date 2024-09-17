T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    number = list(map(int, input().split()))
    for i in range(n-1, 0, -1):
        for j in range(i):
            if number[j] > number[i]:
                number[i], number[j] = number[j], number[i]
    print(f"#{tc}", *number)