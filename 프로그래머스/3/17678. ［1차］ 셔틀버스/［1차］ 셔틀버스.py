# TimeTable Int 형으로 변경 함수
def transform(text):
    type_ = type(text)
    
    # str to int
    if type_ == type("a"):
        return int(text[:2]) * 60 + int(text[3:])
    
    # int to text
    elif type_ == type(1):
        hour = str(text // 60)
        if len(hour) == 1:
            hour = "0" + hour
            
        minute = str(text % 60)
        if len(minute) == 1:
            minute = "0" + minute
            
        return hour + ":" + minute
    

def solution(n, t, m, timetable):
    
    # Int 형으로 변경
    for i in range(len(timetable)):
        timetable[i] = transform(timetable[i])
    
    # Sort
    timetable.sort()
    
    # 콘은 n회 동안 t주기의 m자리에 타야함.
    # n * m 
    bus_time = 540
    crew = 0
    answer = 0
    
    
    # 순회하며 콘이 탈 수 있는지 확인
    for bus in range(n):
        boarding = 0
        while crew < len(timetable):
            # 크루 도착 시간 > 버스 도착 시간
            if timetable[crew] > bus_time:
                break
            else: # 크루 탑승 가능
                boarding += 1 
                crew += 1
                if boarding == m:
                    break
        
        # 막차에서 콘의 탑승 시간 계산
        if bus == n-1:
            # 만차다
            if boarding == m:
                answer = timetable[crew-1] - 1
            # 자리가 남았다
            else:
                answer = bus_time
        # 다음 버스
        bus_time += t
        
    if bus_time == 0:
        return "00:00"
    
    return transform(answer) 