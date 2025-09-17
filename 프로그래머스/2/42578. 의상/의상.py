def solution(clothes):
    dic = {}
    answer = 0
    
    for cloth in clothes:
        # 1개만 입을 때 카운트
        if dic.get(cloth[1]):
            dic[cloth[1]].append(cloth[0])
        else:
            dic[cloth[1]] = [cloth[0]]
    num = 1
    for val in list(dic.values()):
        num *= (len(val) + 1)
    
    return num - 1