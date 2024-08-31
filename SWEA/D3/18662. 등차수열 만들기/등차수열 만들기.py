for tc in range(1, int(input()) + 1):
    a,b,c = map(int,input().split())
    if 2*b == a+c:
        result = 0.0
    elif 2*b > a+c:
        result = (2*b -a-c)/2
    else:
        result = (a+c - 2*b)/2
    print(f"#{tc} {result}")