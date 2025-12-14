def solution(s):
    n = len(s)
    # 짝수
    if n % 2:
        return s[n//2]
    # 홀수
    else:
        return s[n//2 - 1:n//2+1]
    return answer