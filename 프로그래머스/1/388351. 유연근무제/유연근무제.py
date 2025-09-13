def solution(schedules, timelogs, startday):
    def convert(time):
        h, m = int(str(time)[:-2]), time % 100
        if m > 59:
            h += 1
            m = m - 60
        m = str(m)
        if len(m) == 1:
            m = "0" + m
        return int(str(h) + m)
    
    answer = 0
    # i번째 인간이 출근 잘 했나 체크
    for i in range(len(schedules)):
        limit = convert(schedules[i] + 10)
        
        can_event = True
        # 7일 순회
        for j in range(startday, startday + 7):
            
            # 주말은 패스
            if j == 6 or j == 7 or j == 13:
                continue
                
            # 실제 인덱스 값
            j -= startday
            
            # i 인간이 선택한 스케쥴 + 10 보다 크면 탙락
            if timelogs[i][j] > limit:
                can_event = False
                break
            
        if can_event:
            answer += 1
    
    return answer