def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(level, num):
        nonlocal answer 
        
        if level == n:
            if num == target:
                answer += 1
            return
        
        
        dfs(level+1, num + numbers[level])
        dfs(level+1, num - numbers[level])
    
    dfs(0, 0)
    return answer