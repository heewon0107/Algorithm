for tc in range(1, int(input()) + 1):
    N = int(input())
    bills = [0] * 8
    while N >= 50000:
        N -= 50000
        bills[0] += 1
    while N >= 10000:
        N -= 10000
        bills[1] += 1
    while N >= 5000:
        N -= 5000
        bills[2] += 1
    while N >= 1000:
        N -= 1000
        bills[3] += 1
    while N >= 500:
        N -= 500
        bills[4] += 1
    while N >= 100:
        N -= 100
        bills[5] += 1
    while N >= 50:
        N -= 50
        bills[6] += 1
    while N >= 10:
        N -= 10
        bills[7] += 1
    print(f"#{tc}")
    print(*bills)