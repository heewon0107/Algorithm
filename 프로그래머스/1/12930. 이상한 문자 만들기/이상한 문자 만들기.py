def solution(s):
    answer = []
    sequence = True
    for x in s:
        if x == ' ':
            sequence = True
            answer.append(x)
        else:
            if sequence:
                sequence = False
                answer.append(x.upper())
            else:
                sequence = True
                answer.append(x.lower())
            
    return ''.join(answer)