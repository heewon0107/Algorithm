from collections import defaultdict
def solution(players, callings):
    
    grade = defaultdict(int)
 
    # O(50000)
    for i, p in enumerate(players):
        grade[p] = i
    
    # (1,000,000)
    for called in callings:
        
        # grade of called man
        cur_i = grade[called]
        catched = players[cur_i - 1]
        players[cur_i], players[cur_i - 1] = catched, called
        
        # exchange grade
        grade[called] -= 1
        grade[catched] += 1
        
    return players