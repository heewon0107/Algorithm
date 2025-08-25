def is_one_diff(a,b):
    return sum(x != y for x, y in zip(a,b)) == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0] * len(words)
    q =[]
    q.append((begin, 0))
    while q:    
        w, level = q.pop(0)
        if w == target:
            return level
        
        for i, word in enumerate(words):
            if not visited[i] and is_one_diff(w, word):
                visited[i] = 1
                q.append((word, level + 1))
                
                
    return 0
    
    