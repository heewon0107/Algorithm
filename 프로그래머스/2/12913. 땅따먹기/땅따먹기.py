def solution(land):
    # O(100000 * 12)    
    for i in range(1, len(land)):
        for j in range(4):
            x = land[i][j]
            for k in range(4):
                if k == j: 
                    continue
                land[i][j] = max(land[i][j], x + land[i-1][k])
                
    return max(land[-1])