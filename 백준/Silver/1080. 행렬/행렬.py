def solution():
    N, M = map(int, input().split())
    
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(N)]

    op = {
        '0' : '1',
        '1' : '0'
    }

    answer = 0
    # O(2500)
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                answer += 1

                # O(9)
                for r in range(3):
                    for c in range(3):
                        A[i+r][j+c] = op[A[i+r][j+c]]

    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return -1
    
    return answer

print(solution())