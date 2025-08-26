def solution(m, n, puddles):
                                     
    # 각 위치에 가는 최단거리 개수를 동적으로 변경
    arr = [[0] * m for _ in range(n)]
    # 집과 학교 체크
    arr[0][0] = 1
    for y, x in puddles:
        arr[x-1][y-1] = -1
    
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                arr[i][j] = 0
                continue
            if i > 0:
                arr[i][j] += arr[i-1][j]
            if j > 0:
                arr[i][j] += arr[i][j-1]
            arr[i][j] %= 1000000007
    return arr[n-1][m-1]