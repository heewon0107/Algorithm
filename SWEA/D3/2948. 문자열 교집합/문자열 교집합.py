for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    dic = {}
    result = 0
    for x in list(input().split()):
        dic[x] = 1
    
    for x in list(input().split()):
        if dic.get(x):
            result += 1

    print(f'#{tc} {result}')