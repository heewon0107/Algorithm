t = int(input())
for tc in range(1, t + 1):
    m = int(input())
    lst = [list(input().split()) for _ in range(m)]
    string = ""
    for st, num in lst:
        string += st * int(num)

    n = len(string)
    frt = 0
    end = 1
    print(f"#{tc}")
    while n >= 10:
        print(string[frt:10 * end])
        frt += 10
        end += 1
        n -= 10
    print(string[frt:])
