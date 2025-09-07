def solution(s):
    answer = [0,0]
    while s != '1':
        answer[0] += 1
        zero = s.count('0')
        answer[1] += zero
        
        length = len(s) - zero
        s = str(format(length, 'b'))
        

    return answer