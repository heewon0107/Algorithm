def solution(s):
    n = len(s)
    answer = 0
    reverse = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    # O(1000)
    for i in range(n):
        stack = []
        stack.append(s[i])
        can_go = True
        for j in range(1, n):
            idx = (i + j) % n
            c = s[idx]
            # 왼쪽이
            if c in ['[', '{', '(']:
                stack.append(c)
            # 오른쪽이
            else:
                if not stack:
                    can_go = False
                    break
                last = stack.pop()
                if last != reverse[c]:
                    can_go = False
                    break
        if can_go and not stack:
            answer += 1
                
    return answer