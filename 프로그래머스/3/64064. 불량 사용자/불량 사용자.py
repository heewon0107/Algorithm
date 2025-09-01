from itertools import permutations

def solution(user_id, banned_id):
    def is_same(user_id, ban_id):
        if len(user_id) == len(ban_id):
            for i in range(len(user_id)):
                if ban_id[i] == "*":
                    continue
                elif user_id[i] != ban_id[i]:
                    return False
        else:
            return False
                    

        return True
    
     
    if len(user_id) == len(banned_id):
        return 1
    
    lst = []
    for permu in permutations(user_id, len(banned_id)):
        flag = True
        for i in range(len(banned_id)):
            if not is_same(permu[i], banned_id[i]):
                flag = False
        
        if flag:
            if set(permu) not in lst:
                lst.append(set(permu))

    return len(lst)