def solution(name):
    n = len(name)
    answer = 0
    
    # 1. 알파벳 변경 횟수
    for ch in name:
        answer += min(ord(ch) - 65, 26 - (ord(ch) - 65))
    
    # 2. 커서 이동 횟수
    move = n - 1
    for i in range(n):
        ni = i + 1
        
        # 다음 A값 찾기
        while ni < n and name[ni] == 'A':
            ni += 1
        
        # 1. 2*i: -> + <-, n-ni: A까지의 거리
        # 2. 2*(n-ni): <- + ->, 뒤로 갔다가 온 거리
        move = min(move, 2*i + n - ni, i + 2 * (n-ni))
    
    answer += move
    return answer