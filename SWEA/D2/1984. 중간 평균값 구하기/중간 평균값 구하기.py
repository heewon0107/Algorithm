T = int(input())
for tc in range(1, T + 1):
    number = list(map(int, input().split()))
    number.sort()
    print(f"#{tc} {round(sum(number[1:9])/8)}")