from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    # 코스 순회하며 answer에 추가 O(10)
    for c in course:
        dic = defaultdict(int)        
        for o in orders: # O(20 * 10log10)
            for x in combinations(sorted(o), c):
                dic[x] += 1
        
        lst = list(dic.values())
        # 조합 만들 수 없음
        if not lst:
            continue
        # 조합 가능
        else:
            n = max(lst)
            if n < 2:
                continue
            for k, v in dic.items():
                # 최대 값만 후보 코스에 추가
                if v == n:
                    candidate = ''.join(k)
                    answer.append(candidate)
    answer.sort()
    return answer