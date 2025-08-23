def solution(people, limit):
    answer = 0
    people.sort()
    
    light = 0
    heavy = len(people) - 1
    while light <= heavy: 
        # 두 명 탈 수 있다.
        if people[light] + people[heavy] <= limit:
            light += 1
            heavy -= 1
        # 한 명만 탈 수 있다.
        else:
            heavy -= 1
            
        answer += 1
    
    return answer