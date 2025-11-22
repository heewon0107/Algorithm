def LPS(p):
    m = len(p)
    lps = [0] * m
    j = 0
    
    for i in range(1, m):
        # 같지 않다면 j 값은 접두사 길이 만큼 줄여준다.
        while j and p[i] != p[j]:
            j = lps[j-1]
       	# 같은 문자다.
        if p[i] == p[j]:
            j += 1
            lps[i] = j
            
    return lps

def kmp(text, p):
    lps = LPS(p)
    i = j = 0
    cnt = 0
    while i < len(text):
        if text[i] == p[j]:
            i += 1
            j += 1
            if j == len(lps):
                cnt += 1
                j = lps[j-1]
        else:
            if j:
                j = lps[j-1]
            else:
                i += 1
    
    return cnt

for tc in range(1, int(input())+1):
    a = input()
    b = input()
    print(f'#{tc} {kmp(a,b)}')
          
            