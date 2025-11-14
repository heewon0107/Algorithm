T = int(input())
for tc in range(1,T+1):
    N = int(input())
    nums = set()
    i = 1
    while len(nums) < 10:
        x = list(str(N * i))
        nums.update(x)
        i+=1
        
    print(f'#{tc} {N*(i-1)}')