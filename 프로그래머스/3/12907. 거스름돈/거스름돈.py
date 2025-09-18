def solution(n, money):
    # 각 동전 개수
    dp = [1] + [0] * n 
    # 해당 동전의 경우의 수
    for m in money:
        # i번째 경우의 수는 m ~ n + 1
        for i in range(m, n + 1):
            dp[i] += dp[i-m]
    return dp[n % 1000000007]