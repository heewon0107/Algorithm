def team(node):
    visited[node] = 1
    if not adj_lst[node]:
        return

    for i in adj_lst[node]:
        if visited[i] == 1: continue
        team(i)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]
    adj_lst = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    teams = 0

    for x, y in arr:
        adj_lst[x].append(y)
        adj_lst[y].append(x)

    for node in range(1, N + 1):
        if visited[node] == 1: continue
        team(node)
        teams += 1
    print(f"#{tc} {teams}")
