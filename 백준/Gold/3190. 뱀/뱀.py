from collections import deque

N = int(input())
arr = [[0] * N for _ in range(N)]

# 사과
for _ in range(int(input())):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 1

# 방향 전환 정보
L = int(input())
turns = [tuple(input().split()) for _ in range(L)]
turns = [(int(t), d) for t, d in turns]

# 초기 상태
snake = deque([(0, 0)])
direction = 0  # 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
pos = (0, 0)
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution():
    global pos, direction
    total = 0
    turn_idx = 0

    while True:
        total += 1
        nr = pos[0] + delta[direction][0]
        nc = pos[1] + delta[direction][1]

        # 충돌 검사
        if not (0 <= nr < N and 0 <= nc < N) or (nr, nc) in snake:
            return total

        # 이동
        if arr[nr][nc] == 1:
            arr[nr][nc] = 0  # 사과 먹음
        else:
            snake.popleft()  # 꼬리 제거

        pos = (nr, nc)
        snake.append(pos)

        # 방향 전환 시간 체크
        if turn_idx < len(turns) and total == turns[turn_idx][0]:
            if turns[turn_idx][1] == 'D':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
            turn_idx += 1

print(solution())
