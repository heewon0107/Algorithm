def solution(n, results):
    from collections import deque
    answer = 0
    
    win = [[] for _ in range(n + 1)]
    lose = [[] for _ in range(n + 1)]
    
    for winner, loser in results:
        win[winner].append(loser)
        lose[loser].append(winner)
    
    def bfs(node, graph):
        q = deque([node])
        visited = [False] * (n + 1)
        visited[node] = True
        cnt = 0
        while q:
            cur = q.popleft()
            
            for i in graph[cur]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt
    
    for i in range(1, n+1):
        w_cnt = bfs(i, win)
        l_cnt = bfs(i, lose)
        if w_cnt + l_cnt == n-1:
            answer += 1
    
    return answer