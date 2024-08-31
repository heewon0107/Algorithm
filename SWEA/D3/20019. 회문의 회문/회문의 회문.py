T = int(input())
for tc in range(1, T + 1):
    s = input()
    n = len(s)
    result = "NO"
    frt = s[0:int((n-1)/2)]
    rear = s[int((n-1)/2+1):]
    if frt == rear:
        result = "YES"
    print(f"#{tc} {result}")