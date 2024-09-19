op = [1,0]
T = int(input())
for tc in range(1, T + 1):
    memory = list(map(int, input()))
    n = len(memory)
    now = [0] * n
    result = 0
    for i in range(n):
        if now[i] == memory[i]:
            continue
        else:
            result += 1
            for x in range(i,n):
                now[x] = op[now[x]]
    print(f"#{tc} {result}")