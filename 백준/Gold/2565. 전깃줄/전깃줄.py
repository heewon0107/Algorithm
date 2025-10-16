N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

lst.sort(key=lambda x: x[0])

# A 가 증가하기 때문에 B가 증가하는 구간은 겹치지 않음
max_len = 0
cnt = 1

dp = [1] * N
for i in range(N):
    for j in range(i):
        if lst[j][1] < lst[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

l = max(dp)

print(N - l)