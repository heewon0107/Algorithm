for tc in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    LR = [0] + [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * (N + 1)
    for i in range(1, Q + 1):
        L, R = LR[i]
        for box in range(L, R + 1):
            boxes[box] = i
    
    print(f"#{tc}", *boxes[1:])