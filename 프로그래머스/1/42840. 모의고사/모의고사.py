def solution(answers):
    answer = []
    man_1 = 0
    man_2 = 0
    man_3 = 0
    
    pick_1 = [1, 2, 3, 4, 5]
    pick_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pick_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    i = 0
    for a in answers:
        if a == pick_1[i % 5]:
            man_1 += 1
        
        if a == pick_2[i % 8]:
            man_2 += 1
        
        if a == pick_3[i % 10]:
            man_3 += 1
        
        i += 1
        
    if man_1 > man_2:
        if man_1 > man_3:
            answer = [1]
        elif man_1 == man_3:
            answer = [1, 3]
        else:
            answer = [3]
            
    elif man_1 == man_2:
        if man_1 > man_3:
            answer = [1, 2]
        elif man_1 == man_3:
            answer = [1, 2, 3]
        else:
            answer = [3]
    else:
        if man_2 > man_3:
            answer = [2]
        elif man_2 == man_3:
            answer = [2, 3]
        else:
            answer = [3]
    
    return answer