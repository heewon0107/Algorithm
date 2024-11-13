def dfs(cnt):
    global result

    now_num = int("".join(numbers))
    if (cnt, now_num) in visited:
        return

    visited.add((cnt, now_num))
    if cnt == exchange_num:
        result = max(result, now_num)
        return

    for i in range(N-1):
        for j in range(i+1, N):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            dfs(cnt+1)

            numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
for tc in range(1, T+1):
    number, exchange_num = map(int, input().split())
    str_num = (str(number))
    N = len(str_num)
    numbers = [0] * N
    for i in range(N):
        numbers[i] = str_num[i]
    visited = set()

    result = 0
    dfs(0)
    print(f"#{tc} {result}")