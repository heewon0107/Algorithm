def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx, num in enumerate(numbers):
        
        # stack에 인덱스 담아두고 num보다 작은 인덱스 값 갱신
        while stack and numbers[stack[-1]] < num:
            x = stack.pop()
            answer[x] = num
        
        stack.append(idx)
    
    return answer