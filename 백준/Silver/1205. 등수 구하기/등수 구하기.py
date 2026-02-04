def solution():
    N, X, P = map(int, input().split())
    if not N:
        return 1
    ranking = list(map(int, input().split()))

    # Impossible
    if N == P and ranking[-1] >= X:
        return -1
    
    
    for i, v in enumerate(ranking, start=1):
        if X >= v:
            return i
        
    return N + 1

print(solution())