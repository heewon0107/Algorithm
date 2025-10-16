M, N, H = map(int, input().split())

boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 1. 익은 토마토 저장 O(100^3)
tomato = set()
for h in range(H):
    for i in range(N):
        for j in range(M):
            # if tomato
            if boxes[h][i][j] == 1:
                tomato.add((h,i,j))
                
# 2. 토마토 전염
day = 0
while tomato:

    new_tomato = set()
    for h,i,j in tomato:
        # 주변 토마토 검사 상, 하, 좌, 우, 위, 아래
        for dh,di,dj in [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]:
            nh,ni,nj = h+dh, i+di, j+dj

            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and boxes[nh][ni][nj] == 0:
                boxes[nh][ni][nj] = 1
                new_tomato.add((nh,ni,nj))
    

    if not new_tomato:
        break

    tomato = new_tomato
    day += 1

# 3. 안 익은 토마토 점검
def can_result():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                # if tomato
                if boxes[h][i][j] == 0:
                    return False
    return True

print(day if can_result() else -1)