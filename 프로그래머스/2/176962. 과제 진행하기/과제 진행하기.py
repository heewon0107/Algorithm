def transform(hm):
    h, m = hm.split(':')
    h = int(h) * 60
    m = int(m)
    return h + m

from collections import deque

def solution(plans):
    answer = []
    stack = []
    # 시간 순으로 과제 담기
    plans.sort(key=lambda x: transform(x[1]))
        
    
    for i in range(len(plans)):
        name, start, time = plans[i]
        start = transform(start)
        time = int(time)
        # 다음 과제 시작 시간 계산
        if i < len(plans) - 1:
            next_start = transform(plans[i+1][1])
            remain = next_start - start
        else:
            remain = 1e9  # 마지막 과제
        
        # i번째 과제 처리
        if remain >= time:
            answer.append(name)
            remain -= time
            
            # 남은 과제 처리
            while stack and remain > 0:
                s_name, s_time = stack.pop()
                
                if remain >= s_time:
                    answer.append(s_name)
                    remain -= s_time
                else:
                    stack.append((s_name, s_time - remain))
                    break
        else:
            stack.append((name, time - remain))
                   
    while stack:
        answer.append(stack.pop()[0])
    return answer