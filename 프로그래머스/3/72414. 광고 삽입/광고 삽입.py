def solution(play_time, adv_time, logs):
    def convert(time):
        if type(time) is str:
            h = int(time[:2]) * 3600
            m = int(time[3:5]) * 60
            s = int(time[-2:])
            return h + m + s
        
        elif type(time) is int:
            h = time // 3600
            time %= 3600
            m = time // 60
            s = time % 60
            
            return f"{h:02d}:{m:02d}:{s:02d}"
        
    # 1. 시간 => 초 변환 (s)
    play_time = convert(play_time)
    adv_time = convert(adv_time)
        
    # 2. 출입 배열
    time = [0] * (play_time + 2)
    for log in logs:
        s, e = map(convert, log.split('-'))
        time[s] += 1
        time[e] -= 1
    
    # 3. 초 당 시청자 수 배열
    for i in range(1, play_time + 1):
        time[i] += time[i - 1]
        
    # 4. 누적 시청자 수 배열
    viewer = [0] * (play_time + 2)
    for i in range(1, play_time + 2):
        viewer[i] += viewer[i-1] + time[i - 1]
        
    # 5. 광고시간 책정
    ad_start = 0
    max_val = 0
    for t in range(play_time - adv_time + 1):
        total = viewer[t + adv_time] - viewer[t]
        if total > max_val:
            max_val = total
            ad_start = t
    
    # 6. 변환
    return convert(ad_start)