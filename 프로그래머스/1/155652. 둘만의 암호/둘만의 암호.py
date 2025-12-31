def solution(s, skip, index):
    answer = ''
    n = len(s)
    # 모든 s문자열 순회
    for i in range(n):
        cur = s[i]
        idx = ord(cur)
        cnt = index
        while cnt:
            idx += 1
            
            if idx > 122:
                idx -= 26
            
            tar = chr(idx)
            if tar not in skip:
                cnt -= 1
            
        answer += tar
    return answer