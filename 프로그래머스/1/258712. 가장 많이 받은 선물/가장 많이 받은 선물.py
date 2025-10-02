def solution(friends, gifts):
        
    from collections import defaultdict
    
    # 선물 준 사람 넣기
    dic = defaultdict(list)
    # 준 선물 수
    give_dic = defaultdict(int)
    # 받은 선물 수
    receive_dic = defaultdict(int)
    
    for gift in gifts: # O(30000)
        giver, receiver = gift.split(" ")
        dic[giver].append(receiver)
        give_dic[giver] += 1
        receive_dic[receiver] += 1
    
    
    result = 0
    # friends 순회하며 내가 받을 선물 기록
    for friend in friends: # O(50)
        # 한 명이 받는 선물
        cur_gived = 0
        # 내가 선물 준 사람들
        others = dic[friend]
        
        for f in friends: # O(50)
            if f == friend:
                continue
            
            # 내가 준 선물 수
            i_give = others.count(f)
            # 내가 받은 선물 수
            he_give = dic[f].count(friend)
            
            # 두 사람 간 선물 주고받은 기록 a > b
            if i_give > he_give:
                cur_gived += 1
            # 두 사람 간 선물 주고 받은 기록 0 or a == b
            elif i_give == he_give:
                # 선물지수 큰 사람 <- 작은 사람
                # 선물지수: 준 선물 - 받은 선물
                if give_dic[friend] - receive_dic[friend] > give_dic[f] - receive_dic[f]:
                    cur_gived += 1
        result = max(cur_gived, result)
    
    # 선물 가장 많이 받을 친구의 선물 수
    return result