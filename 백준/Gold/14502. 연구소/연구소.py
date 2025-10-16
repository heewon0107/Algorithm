from itertools import combinations
import copy
from collections import deque

def spread(lab):    
    q = deque()
    for i in range(N):
        for j in range(M):
            if area[i][j] == 2:
                q.append((i,j))

    while q:
        i, j = q.popleft()
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and not lab[ni][nj]:
                lab[ni][nj] = 2
                q.append((ni,nj))

    return lab

def calculator_safe(lab):
     return sum(i.count(0) for i in lab)


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)] 
zeros = [(i,j) for i in range(N) for j in range(M) if area[i][j] == 0]



result = 0
for walls in combinations(zeros, 3):
    lab = copy.deepcopy(area)
    for i, j in walls:
        lab[i][j] = 1
    
    result = max(calculator_safe(spread(lab)),result)

print(result)