def solution(food):
    answer = []
    for i in range(1, len(food)):
        dish = food[i]
        dividen_food = dish // 2
        if dividen_food:
            for _ in range(dividen_food):
                answer.append(i)
        
    answer = list(map(str, answer))
    return ''.join(answer) + '0' + ''.join(answer[::-1])