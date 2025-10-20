def solution(number, k):
    stack = []
    for num in number:
        while stack and num > stack[-1] and k:
            stack.pop()
            k -= 1
        stack.append(num)
    
    if k:
        stack = stack[:-k]
    
    return ''.join(stack)