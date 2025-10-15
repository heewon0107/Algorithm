def solution():
    N, M, V = map(int, input().split())

    # 양방향 인접리스트
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    df = [V]
    visited = [0] * (N+1)
    def dfs(i):
        
        graph[i].sort()
        for next_node in graph[i]:
            if not visited[next_node]:
                visited[next_node] = 1
                df.append(next_node)
                dfs(next_node)


    visited[V] = 1
    dfs(V)

    from collections import deque
    bf = [V]
    visited = [0] * (N+1)
    q = deque()
    q.append(V)
    visited[V] = 1

    while q:
        
        node = q.popleft()
        graph[node].sort()
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                bf.append(next_node)
                visited[next_node] = 1

    print(*df)
    print(*bf)

solution()