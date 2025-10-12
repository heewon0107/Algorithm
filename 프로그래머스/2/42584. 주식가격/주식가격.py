def solution(prices):
    stack = []
    n = len(prices)
    answer = [0] * n
    
    for i, price in enumerate(prices):
        
        # 가격이 깍임
        while stack and prices[stack[-1]] > price:
            j = stack.pop()

            answer[j] = i - j
            
        stack.append(i)
    
    
    while stack:
        i = stack.pop()
        answer[i] = n - i - 1
        
    return answer