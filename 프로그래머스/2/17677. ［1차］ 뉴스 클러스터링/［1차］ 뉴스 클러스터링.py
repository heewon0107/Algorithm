from collections import Counter

def solution(str1, str2):
    answer = 0
    a = []
    b = []
    
    for i in range(1, len(str1)):
        s = str1[i-1] + str1[i]
        if s.isalpha():
            a.append(s.lower())
            
    for i in range(1, len(str2)):
        s = str2[i-1] + str2[i]
        if s.isalpha():
            b.append(s.lower())
    
    a = Counter(a)
    b = Counter(b)
    inter = a & b
    union = a | b

    if not union:
        return 65536
    
    return int(sum(inter.values()) / sum(union.values())  * 65536)