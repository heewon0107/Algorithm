from collections import defaultdict

def solution(info, edges):
    
    def dfs(sheep, wolf, cur_node, next_nodes):
        nonlocal max_sheep
        
        if sheep <= wolf:
            return
        
        max_sheep = max(sheep, max_sheep)
        
        for i, next_node in enumerate(next_nodes):
            new_next = next_nodes[:i] + next_nodes[i+1:]
            new_next += graph[next_node]
            
            if info[next_node] == 0:
                dfs(sheep + 1, wolf, next_node, new_next)
            else:
                dfs(sheep, wolf + 1, next_node, new_next)
            
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    
    max_sheep = 0
    
    dfs(1, 0, 0, graph[0])
    
    return max_sheep