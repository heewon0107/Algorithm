def solution(numbers):
    answer = []
    for n in numbers:   # O(10^5)
        if not n % 2:
            answer.append(n+1)
        else:
            b = '0' + bin(n)[2:]
            idx = b.rfind('0')
            b = b[:idx] + '10' + b[idx+2:]
            answer.append(int(b, 2))
            
    return answer