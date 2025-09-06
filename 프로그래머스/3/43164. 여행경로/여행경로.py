def solution(tickets):
    from collections import defaultdict

    graph = defaultdict(list)
    # 항공권 정보 그래프에 담기 (도착지를 사전순으로 정렬하기 위해 reverse 사용)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    path = []

    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        path.append(airport)
        
    dfs("ICN")
    
    return path[::-1]
