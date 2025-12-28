from collections import deque

def solution(N, road, K):
    visited = [1e9] * (N+1)
    visited[1] = 0
    
    lst = [[] for _ in range(N+1)]
    for x, y, z in road:
        lst[x].append((y, z))
        lst[y].append((x, z))
        
    q = deque([(1, 0)])
    while q:
        node, t = q.popleft()
        
        for next_node, time in lst[node]:
            total = time + t
            # K 값 초과
            if total > K:
                continue
                
            # 이번 경로가 더 오래걸림
            if visited[next_node] < total:
                continue
            else: # 최단 경로를 찾았다.
                visited[next_node] = total
                cur = (next_node, total)
                q.append(cur)
    not_go = visited.count(1e9)    
    return N - not_go + 1