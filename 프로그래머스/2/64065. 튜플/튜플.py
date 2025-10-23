def solution(s):
    lst = []
    s = s[1:-1]
    i = 0
    while i < len(s):
        
        if s[i] == '{':
            first = i+1
            # 닫힐 때까지
            while s[i] != '}':
                i += 1
            lst.append(list(map(int, s[first:i].split(','))))
        i += 1
    
    lst.sort(key=lambda x: len(x))
    
    answer = []
    for l in lst:
        for x in l:
            if x not in answer:
                answer.append(x)
    # '{' 나오면 '}' 나올 때까지 isdigit면 [].append
    return answer