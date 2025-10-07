def solution(k, dungeons):
    def dfs(visited, level, dungeons, k):
        nonlocal answer
        nonlocal n
        answer = max(level, answer)
        
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = 1
                dfs(visited, level + 1, dungeons, k - dungeons[i][1])
                visited[i] = 0
    
    answer = 0
    n = len(dungeons)
    visited = [0] * n
    
    dfs(visited, 0, dungeons, k)
            
    return answer