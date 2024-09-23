T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    lst = [i + 1 for i in range(12)]
    result = 0
    for i in range(1 << 12):
        subset = []
        subset_sum = 0
        for j in range(12):
            if i & (1 << j):
                subset.append(lst[j])
                subset_sum += lst[j]

        if len(subset) == n and subset_sum == k:
            result += 1
    print(f"#{tc} {result}")