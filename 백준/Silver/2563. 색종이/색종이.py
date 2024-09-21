white = [[0] * 100 for _ in range(100)]
for _ in range(int(input())):
    r, c = map(int, input().split())
    for i in range(r, r+10):
        for j in range(c, c+10):
            white[i][j] = 1
result = 0
for i in range(100):
    for j in range(100):
        if white[i][j] == 1:
            result += 1
print(result)