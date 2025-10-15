from collections import defaultdict

def solution():
    n = input()
    if len(n) == 1:
        return n.upper()

    dic = defaultdict(int)

    for i in n:
        dic[i.upper()] += 1
    
    if len(dic) == 1:
        return list(dic.keys())[0]
        

    lst = sorted(dic.items(), key=lambda x:x[1], reverse=True)

    if lst[0][1] == lst[1][1]:
        return '?'
    else:
        return lst[0][0]
    
print(solution())