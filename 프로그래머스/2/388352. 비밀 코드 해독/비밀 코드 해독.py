from itertools import combinations

def solution(n, q, ans):
    m = len(q)
    
    # 1~n 조합 생성
    candidates = list(combinations(range(1, n+1), 5))
    
    candi_lst = []
    
    # C(30, 5) O(143,000)
    for code in candidates:
        ok = True
        # O(10)
        for i in range(m):
            # 조합과 입력 값의 교집합 개수
            cnt = len(set(code) & set(q[i]))
            
            # 시스템 응답과 불일치
            if cnt != ans[i]:
                ok = False
                break
        # 시스템 응답과 일치                
        if ok:
            candi_lst.append(code)
            
    return len(candi_lst)