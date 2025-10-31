from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    wating = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    w = 0
    
    while wating or any(bridge):
        answer += 1
        x = bridge.popleft()
        if x:
            w -= x
        
        # 대기 트럭 있다.
        if wating and wating[0]:
            if w + wating[0] <= weight:
                truck = wating.popleft()
                w += truck
                bridge.append(truck)
            else:
                bridge.append(0)
        
        
    return answer