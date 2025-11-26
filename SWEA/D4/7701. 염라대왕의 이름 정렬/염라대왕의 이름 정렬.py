for tc in range(1,int(input())+1):
    N = int(input())
    names = set()
    for _ in range(N):
        names.add(input())
    names = list(names)
    names = sorted(names, key=lambda x: (len(x), x))

    print(f'#{tc}')

    for name in names:
        print(name)