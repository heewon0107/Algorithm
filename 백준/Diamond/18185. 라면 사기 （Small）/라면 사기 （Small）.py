N = int(input())
factories = list(map(int, input().split()))

cost = 0
idx = 0

while idx < N:
    cur = factories[idx]
    # 안 사도 됨
    if not cur:
        idx += 1
        continue

    # 함께 사는 방법: i+1번째에 살게 있어야한다.
    if idx + 1 < N:
        next_a = factories[idx + 1]
        # 1. 살 게 없다면 i번째만 구매
        if not next_a:
            cost += cur * 3
            idx += 2

        # 2. i+1 번째에 살게 있다.
        else:
            if idx + 2 < N:
                next_b = factories[idx+2]
                # i, i+1만 구매
                if not next_b:
                    purchase_num = min(next_a, cur)
                    factories[idx] -= purchase_num
                    factories[idx + 1] -= purchase_num
                    cost += purchase_num * 5
                
                # i+1 > i+2
                elif next_a > next_b:
                    purchase_num = min(cur, next_a - next_b)
                    factories[idx] -= purchase_num
                    factories[idx+1] -= purchase_num
                    cost += purchase_num * 5
                    
                # 셋 다 구매
                else:
                    purchase_num = min(next_a, next_b, cur)
                    factories[idx] -= purchase_num
                    factories[idx + 1] -= purchase_num
                    factories[idx + 2] -= purchase_num
                    cost += purchase_num * 7
            # i, i+1
            else:
                purchase_num = min(next_a, cur)
                factories[idx] -= purchase_num
                factories[idx + 1] -= purchase_num
                cost += purchase_num * 5


    # 마지막 인덱스
    else:
        cost += cur * 3
        break
    
print(cost)