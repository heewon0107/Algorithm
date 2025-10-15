N, K = map(int, input().split())

items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for weight, value in items:

    # K ~ weight-1
    for w in range(K, weight-1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)


print(dp[K])