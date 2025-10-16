def solution():
    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]
    lst.sort(key=lambda x: (x[1], x[0]))

    result = 1
    end = lst[0][1]
    for i in range(1, len(lst)):
        if lst[i][0] < end:
            continue

        result += 1
        end = lst[i][1]

    return result
print(solution())