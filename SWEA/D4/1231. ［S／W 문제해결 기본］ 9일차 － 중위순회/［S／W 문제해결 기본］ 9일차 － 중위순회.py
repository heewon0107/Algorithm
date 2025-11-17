def in_order(node):
    global result

    if not node:
        return

    in_order(left[node])
    result += tree[node]
    in_order(right[node])

    return result


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for _ in range(N):
        lst = list(input().split())
        # 노드
        cur = int(lst[0])
        tree[cur] = lst[1]
        if len(lst) > 2:
            left[cur] = int(lst[2])
        
        if len(lst) == 4:
            right[cur] = int(lst[3])
    result = ''    
    in_order(1)
    print(f'#{tc} {result}')