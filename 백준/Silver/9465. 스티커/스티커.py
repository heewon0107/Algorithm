import sys
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))

    for j in range(1, N):
        dp[0][j] = max(dp[1][j-1] + dp[0][j], dp[0][j-1])
        dp[1][j] = max(dp[0][j-1] + dp[1][j], dp[1][j-1])
    
    answer.append(str(max(dp[0][N-1], dp[1][N-1])))
    
print('\n'.join(answer))