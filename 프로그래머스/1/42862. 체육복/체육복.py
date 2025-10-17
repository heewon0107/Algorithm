def solution(n, lost, reserve):
    
    state = [1] * (n+2)
    state[0] = 0
    state[-1] = 0
    for num in lost:
        state[num] -= 1
    
    for num in reserve:
        state[num] += 1
    
    # state 0인 친구를 찾고 앞에서 먼저 빌리고 뒤에서 빌림
    
    for i in range(1, n+1):
        if not state[i]:
            # 앞 친구
            if state[i-1] == 2:
                state[i-1] -= 1
                state[i] = 1
            # 뒤 친구
            elif state[i+1] == 2:
                state[i+1] -= 1
                state[i] = 1

                
    return sum(1 for i in state if i > 0)