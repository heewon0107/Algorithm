def solution(s):
    answer = 0
    n = len(s)
    
    def pailndrom(left, right):
        while 0 <= left and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left -1
    
    for i in range(n):
        len1 = pailndrom(i,i)
        len2 = pailndrom(i, i+1)
        answer = max(answer, len1, len2)
        
    return answer