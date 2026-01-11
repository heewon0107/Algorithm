M, N = map(int, input().split())
snacks = list(map(int, input().split()))
snacks.sort(reverse=True)
result = 0

l, r = 1, snacks[0]
# O(log1e9)
while l <= r:
    mid = (l+r) // 2
    cnt = 0
    
    for snack in snacks:
        num = snack // mid
        cnt += num

        if cnt >= M or not num:
            break
    
    # 과자 길이가 커서 나눌 수 없다.
    if cnt < M:
        r = mid - 1
    # 나눌 수 있다 더 최댓값 찾아보자
    else:
        l = mid + 1
        result = mid
    
print(result)