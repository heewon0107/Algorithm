def harvest(cur_honey):
    global M, C
    max_profit = 0
    # O(150)
    for subset in range(1 << M):
        honey = 0
        profit = 0
        for i in range(M):
            if subset & (1 << i):
                honey += cur_honey[i]
                profit += cur_honey[i] ** 2

        if honey <= C:
            max_profit = max(profit, max_profit)

    return max_profit

for tc in range(1, int(input()) + 1):
    # N = 벌집 개수
    # M = 가능한 '가로'로 '연속'된 채취 벌통의 수
    # C = 한 벌통의 최대값
    # 일꾼은 2명, 채취한 벌통은 겹치면 안됨 
    N, M, C = map(int, input().split())
    honey_lst = [list(map(int, input().split())) for _ in range(N)]
    
    harvest_lst = [[0] * (N - M + 1) for _ in range(N)]
    # O(100 * harvest)
    for i in range(N):
        for j in range(N - M + 1):
            harvest_lst[i][j] = harvest(honey_lst[i][j:j+M])
    

    result = 0
    for i in range(N):
        for j in range(N - M + 1):
            first = harvest_lst[i][j]

            for r in range(N):
                for c in range(N - M + 1):

                    # 같은 위치
                    if i == r and j == c:
                        continue

                    # 겹친 위치
                    if i == r and abs(j - c) < M:
                        continue         

                    profit = first + harvest_lst[r][c]
                    result = max(result, profit)
    
    print(f'#{tc} {result}')