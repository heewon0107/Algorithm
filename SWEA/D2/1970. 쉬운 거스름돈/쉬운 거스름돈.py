T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bill = [0] * 8
    num = 0
    for x in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        while x <= N:
            bill[num] += 1
            N -= x
        num += 1
    print(f"#{tc}")
    print(*bill)
