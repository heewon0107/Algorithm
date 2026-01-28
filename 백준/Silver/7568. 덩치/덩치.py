import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = []
for i in range(N):
    cnt = 1
    # 대상
    height, weight = arr[i]
    for j in range(N):
        if i == j:
            continue
        # 비교
        if height < arr[j][0] and weight < arr[j][1]:
            cnt += 1
    answer.append(cnt)

print(' '.join(map(str, answer)))