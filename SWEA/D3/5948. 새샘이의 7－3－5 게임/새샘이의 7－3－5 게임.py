answer = [0]

def sasam(n, idx, total):
    global sum_list
    if n == 3:
        if total not in sum_list:
            sum_list.append(total)
    else:
        remains = 3 - (n+1)
        for i in range(idx, 7 - remains):
            sasam(n + 1, i + 1, total + arr[i])

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    sum_list = []
    sasam(0, 0, 0)
    sum_list.sort(reverse=True)
    answer.append(sum_list[4])

for tc in range(1, T+1):
    print(f"#{tc} {answer[tc]}")