from collections import deque

def dijkstra(s, n, graph):
    dijk = [1e9] * (n+1)
    dijk[s] = 0
    q = deque()
    q.append((0, s))
    
    while q:
        fare, node = q.popleft()
        # 이미 최소값
        if dijk[node] < fare:
            continue
    
        for next_fare, next_node in graph[node]:
            new_fare = fare + next_fare
            if new_fare < dijk[next_node]:
                dijk[next_node] = new_fare
                q.append((new_fare, next_node))
    return dijk
       
def solution(n, s, a, b, fares):
    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for start, end, fare in fares:
        graph[start].append((fare, end))
        graph[end].append((fare, start))
    
    dijk_s = dijkstra(s, n, graph) # 출발지부터 모든 노드에 가는 최단거리
    dijk_a = dijkstra(a, n, graph) # a부터 모든 노드에 가는 최단거리
    dijk_b = dijkstra(b, n, graph) # b부터 모든 노드에 가는 최단거리
    
    answer = 1e9
    for i in range(1, n+1):
        answer = min(answer, dijk_s[i] + dijk_a[i] + dijk_b[i])
    return answer