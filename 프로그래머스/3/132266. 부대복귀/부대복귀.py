from collections import deque

def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n+1)]
    # 양방향 그래프 생성
    for x, b in roads:
        graph[x].append(b)
        graph[b].append(x)
    
    # q
    q = deque([destination])
    
    distance = [-1] * (n+1)
    distance[destination] = 0
    
    while q:
        cur = q.popleft()
        
        for node in graph[cur]:
            # 방문전
            if distance[node] == -1:
                distance[node] = distance[cur] + 1
                q.append(node)
            
            
        
        
    return [distance[s] for s in sources]