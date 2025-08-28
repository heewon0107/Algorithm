def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    
    answer = 0
    for into, out in routes:
        if into > camera:
            camera = out
            answer += 1
        
    return answer