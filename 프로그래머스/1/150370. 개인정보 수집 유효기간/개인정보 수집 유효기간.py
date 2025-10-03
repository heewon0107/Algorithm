def solution(today, terms, privacies):
    from collections import defaultdict
    
    def trans(day):
        y, m, d = map(int, day.split("."))
        # 1년은 12달, 12달은 28일
        return y * 12*28 + m*28 + d
    
    # 모든 달은 28일까지!!
    
    today = trans(today)
    dic = defaultdict(int)
    for t in terms:
        c, n = t.split(" ")
        dic[c] = int(n) * 28
        
    result = []
    for i, p in enumerate(privacies, start=1):
        d, c = p.split(' ')
        if trans(d) + dic[c] <= today:
            result.append(i)
    
    return result