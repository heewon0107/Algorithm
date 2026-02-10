def solution(number):
    def triple(N, i, total, cnt):
        nonlocal answer
        
        # Update point
        if cnt == 3 and total == 0:
            answer += 1
            return
        
        # End point
        if i == N:
            return
        
        
        # Push cur
        triple(N, i+1, total + number[i], cnt + 1)
        
        # Not push cur
        triple(N, i+1, total, cnt)
        
    answer = 0
    N = len(number)
    triple(N, 0, 0, 0)
    return answer