def solution(order):
    N = len(order)
    container = [i for i in range(N, 0, -1)]
    sub_container = []
    
    answer = 0
    idx = 0
    while idx < N:
        box = order[idx] 
        
        # 보조 컨테이너에 있다.
        if sub_container and sub_container[-1] == box:
            sub_container.pop()
            answer += 1
            idx += 1
            continue
            
        can_go = False
        while container:
            cur = container.pop()
            # 컨테이너에서 빼거나
            if cur == box:
                answer += 1
                can_go = True
                break
            else:
                sub_container.append(cur)
        if can_go:
            idx += 1
        else:
            break
    
    return answer