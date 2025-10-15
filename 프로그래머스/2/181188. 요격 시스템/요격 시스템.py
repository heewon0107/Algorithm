def solution(targets):
    answer = 1
    
    # 정렬
    targets.sort(key=lambda x:(x[1]))
    last = targets[0][1]
    
    for i in range(1, len(targets)):
        if targets[i][0] < last:
            continue
        else:
            last = targets[i][1]
            answer += 1
    
    return answer