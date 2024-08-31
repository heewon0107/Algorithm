T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N=주머니 개수, K=나눠 줄 주머니 개수
    candy = list(map(int, input().split()))  # 주머니속 사탕 개수
    candy.sort()
    result = 10**9
    for i in range(N - K +1):
        diff = candy[i+K-1] - candy[i]
        if result > diff:
            result = diff
    print(f"#{tc} {result}")