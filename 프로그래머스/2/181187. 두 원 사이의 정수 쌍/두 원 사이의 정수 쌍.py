import math

def solution(r1, r2):
    answer = 0
    for x in range(1, r2+1):
        # y좌표 s~e
        if x < r1:
            s = math.ceil(math.sqrt(r1**2 - x**2))
        else:
            s = 0
        
        e = int(math.sqrt(r2**2 - x**2))
        answer += e-s+1
        
        
        
    return answer*4