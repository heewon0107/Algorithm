for tc in range(1, int(input())+1):
    N, K = map(int, input().split())

    # 1. K 부피 만큼의 DP 배열
    dp = [0] * (K+1)

    # 2. N만큼 DP 갱신 
    for _ in range(N): # O(100*1000)
        V, C = map(int, input().split())

        for w in range(K, V-1, -1):
            dp[w] = max(dp[w], dp[w-V] + C)

    print(f'#{tc} {max(dp)}')
