answer = [0]


T = int(input())
for t in range(1, T+1):
    char = input()
    result = ""
    for x in char:
        if x not in "aeiou":
            result += x
    answer.append(result)
for tc in range(1, T+1):
    print(f"#{tc} {answer[tc]}")