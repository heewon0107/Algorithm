def cal(n, total,calcul):
    global max_value, min_value
    if n == N-1:
        if total > max_value:
            max_value = total
        if total < min_value:
            min_value = total
        return

    for i in range(4):
        if calculator[i] == 0:
            continue
        elif i == 0:
            num = numbers.pop()
            calcul[i] -= 1
            cal(n+1, total + num, calcul)
            numbers.append(num)
            calcul[i] += 1
        elif i == 1:
            num = numbers.pop()
            calcul[i] -= 1
            cal(n + 1, total - num, calcul)
            numbers.append(num)
            calcul[i] += 1
        elif i == 2:
            num = numbers.pop()
            calcul[i] -= 1
            cal(n + 1, total * num, calcul)
            numbers.append(num)
            calcul[i] += 1
        elif i == 3:
            num = numbers.pop()
            calcul[i] -= 1
            cal(n + 1, int(total / num), calcul)
            numbers.append(num)
            calcul[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    calculator = list(map(int, input().split()))
    numbers = list(reversed(list(map(int, input().split()))))
    max_value = -1e9
    min_value = 1e9
    cal(0, numbers.pop(), calculator)
    print(f"#{tc} {max_value - min_value}")