T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    price = list(map(int, input().split()))
    max_val = 0
    cost = 0
    for j in range(n - 1, -1, -1):
        if price[j] >= max_val:
            max_val = price[j]
        else:
            cost += max_val - price[j]
    print(f"#{tc} {cost}")