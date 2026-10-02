def solution(k, dungeons):
    
    clear = 0
    N = len(dungeons)
    visited = [0] * N
    
    def dfs(level, fatigue, cnt):
        nonlocal clear, N

        clear = max(clear, cnt)
        
        # 남은 곳 다 가도 안됨
        # if N - level < clear:
        #     return
        
        for i in range(N):
            minimum_fatigue, cost_fatigue = dungeons[i]
            if not visited[i] and minimum_fatigue <= fatigue:
                visited[i] = 1
                dfs(level+1, fatigue - cost_fatigue, cnt + 1)
                visited[i] = 0
            
    dfs(0, k, 0)
    
    return clear

#     def dfs(visited, level, dungeons, k):
#         nonlocal answer
#         nonlocal n
#         answer = max(level, answer)
        
#         for i in range(n):
#             if not visited[i] and k >= dungeons[i][0]:
#                 visited[i] = 1
#                 dfs(visited, level + 1, dungeons, k - dungeons[i][1])
#                 visited[i] = 0
    
#     answer = 0
#     n = len(dungeons)
#     visited = [0] * n
    
#     dfs(visited, 0, dungeons, k)
            
#     return answer