
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
r_chk = [0] * n
c_chk = [0] * m
for i in range(n):
    for j in range(m):
        if board[i][j] == "X":
            r_chk[i] = 1
            c_chk[j] = 1
r = n - sum(r_chk)
c = m - sum(c_chk)

cnt = max(r, c)


print(cnt)