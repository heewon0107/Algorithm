import copy

def solution(n, wires):
    result = 1e9
    
    def dfs(node):
        visited[node] = 1
        cnt = 1
        for next_node in tree[node]:
            if not visited[next_node]:
                cnt += dfs(next_node)
        
        return cnt
    
    # 양방향 그래프
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # n까지의 wire 짜르고 graph 탐색
    for i in range(n-1):
        a, b = wires[i]
        tree = copy.deepcopy(graph)
        tree[a].remove(b)
        tree[b].remove(a)
        
        visited = [0] * (n+1)

        cnt = dfs(a)
        
        diff = abs(n - 2*cnt)
        result = min(result, diff)
        
    return result