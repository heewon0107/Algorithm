def solution(k, d):
    answer = 0
    d2 = d * d
    
    x = 0
    # O(log2 1000000)
    while x <= d:
        # x^2 + y^2 <= d^2
        max_y = int((d2 - x*x) ** 0.5)
        # +1 (x축 좌표 포함)
        answer += (max_y // k) + 1
        x += k
    
    return answer
