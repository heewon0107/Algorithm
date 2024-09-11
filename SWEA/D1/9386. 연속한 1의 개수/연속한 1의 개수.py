result = []
for tc in range(1, int(input())+1):
    n = int(input())
    sequence = 0
    cur = 0
    for i in input():
        if i == "1":
            sequence += 1
            if sequence > cur:
                cur = sequence
        else:
            sequence = 0
    result.append(cur)
for idx, r in enumerate(result):
    print(f"#{idx + 1} {r}")