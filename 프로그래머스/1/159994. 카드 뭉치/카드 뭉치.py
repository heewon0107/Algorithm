def solution(cards1, cards2, goal):
    one = 0
    two = 0
    g = 0
    
    while (one < len(cards1) or two < len(cards2)) and g < len(goal):
        
        if one < len(cards1) and cards1[one] == goal[g]:
            one += 1
            g += 1
        elif two < len(cards2) and cards2[two] == goal[g]:
            two += 1
            g += 1
        else:
            return 'No'
    return 'Yes'