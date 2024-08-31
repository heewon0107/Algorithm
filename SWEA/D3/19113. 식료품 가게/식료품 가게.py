T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    discount = list(map(int, input().split()))
    # 정상가격 품목을 빼버림
    for i in range(N): # 품목 개수
        jdx = i+1
        while True:
            # 정상 품목이면 팝해
            if discount[jdx] == discount[i]*4/3:
                discount.pop(jdx)
                break
            jdx += 1
    print(f"#{tc}", *discount)