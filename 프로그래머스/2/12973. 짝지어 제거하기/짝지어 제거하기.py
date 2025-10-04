def solution(s):
    
    stack = []
    i = 0
    while i < len(s):
        # 비교할 대상이 있나
        if stack:
            # 마지막 비교 대상이 중복되었나
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
        i += 1
    return 0 if stack else 1
            