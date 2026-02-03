def solution():
    N = int(input())
    board = [input() for _ in range(N)]

    # Find position of head O(N^2)
    def find_head():
        for i in range(N):
            for j in range(N):
                if board[i][j] == '*':
                    return i, j

    # Measure Length O(N)
    def measure(r, c, dr, dc):
        cnt = 0
        while 0 <= r < N and 0 <= c < N and board[r][c] == '*':
            cnt += 1
            r += dr
            c += dc
        return cnt

    # Measure Length of waist and Get End Position O(N)
    def m_waist(r, c, dr, dc):
        cnt = 0
        while 0 <= r < N and 0 <= c < N and board[r][c] == '*':
            cnt += 1
            r += dr
            c += dc
        return cnt, r, c

    # 1. Find position of Head
    r, c = find_head()

    # 2. Find heart of Head
    heart_r, heart_c = r + 1, c

    # 3. Measure each part
    l_arm = measure(heart_r, heart_c - 1, 0, -1)
    r_arm = measure(heart_r, heart_c + 1, 0, 1)
    waist, r, c = m_waist(heart_r + 1, heart_c, 1, 0)
    l_leg = measure(r, c - 1, 1, 0)
    r_leg = measure(r, c + 1, 1, 0)

    print(heart_r + 1, heart_c + 1)
    print(l_arm, r_arm, waist, l_leg, r_leg)

solution()