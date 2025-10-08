import math
def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    for i in range(n):
        progress = progresses[i]
        speed = speeds[i]
        left = 100 - progress
        day = math.ceil(left / speed)
        progresses[i] = day
    
    today = 0
    idx = -1
    for i in range(n):
        # 개발됨
        if progresses[i] <= today:
            answer[idx] += 1
        # 배포
        else:
            answer.append(1)
            today = progresses[i]
            idx += 1
    return answer