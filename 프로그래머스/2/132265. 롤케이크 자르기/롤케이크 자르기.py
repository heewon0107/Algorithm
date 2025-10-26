from collections import defaultdict
def solution(topping):
    answer = 0
    
    left = set()
    right = defaultdict(int)
    
    for t in topping:
        right[t] += 1
    
    for i in range(len(topping)-1):
        t = topping[i]
        
        left.add(t)
        right[t] -= 1
        
        if not right[t]:
            del right[t]
        
        if len(left) == len(right):
            answer += 1
        
        
    return answer