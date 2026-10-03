def solution(numbers, target):
    
    def dfs(n, total):
        nonlocal N, target, answer
        
        if n == N:
            if total == target:
                answer += 1
            return
        
        dfs(n + 1, total + numbers[n])
        dfs(n + 1, total - numbers[n])
        
    answer = 0
    N = len(numbers)
    dfs(0, 0)
    return answer