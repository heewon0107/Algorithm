import math

N = int(input())
remains = list(map(int, input().split()))
plans = list(map(int, input().split()))

lst = [[r, p] for r, p in zip(remains, plans)]
lst.sort(key=lambda x: (x[1], x[0]))

max_day = lst[0][0]
th = lst[0][1]
result = 0

for i in range(N):

    if th > lst[i][0]:
        tmp = math.ceil((th-lst[i][0]) / 30)
        result += tmp
        lst[i][0] += tmp *30
    
    max_day = max(max_day, lst[i][0])

    if i+1 < N and lst[i][1] != lst[i+1][1]:
        th = max(max_day, lst[i+1][1])


print(result)