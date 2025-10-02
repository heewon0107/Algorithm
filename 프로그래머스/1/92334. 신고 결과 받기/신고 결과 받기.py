def solution(id_list, report, k):
    from collections import defaultdict
    
    # 신고 당한 수 dict
    claim_dic = defaultdict(set)
    
    # 메일 수 dict
    mail_dic = defaultdict(int)
    
    # 신고
    for r in report:
        a, b = r.split(" ")
        claim_dic[b].add(a)
    
    # 메일
    for v in claim_dic.values():
        if len(v) >= k:
            for man in v:
                mail_dic[man] += 1
            
    return [mail_dic[id] for id in id_list]