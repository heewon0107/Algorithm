from collections import deque
def solution(n, edge):
    answer = 0
    lst = [[] for _ in range(n+1)]
    for x, y in edge:
        lst[x].append(y)
        lst[y].append(x)
    
    # BFS
    q = deque()
    visited = [False] * (n + 1)
    visited[1] = True
    q.append((1, 0)) 
    max_val = 0
    while q:
        node, level = q.popleft()
        
        if level == max_val:
            answer += 1
        elif level > max_val:
            max_val = level
            answer = 1            
            
           
        for next_node in lst[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, level + 1))
        
    return answer