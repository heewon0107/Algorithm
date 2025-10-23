def solution(fees, records):
    # fees
    # 0: 기본 시간(분), 1: 기본 요금(원), 2: 단위 시간(분), 3: 단위 요금(원)
    
    # records
    # 0: 시각(시:분 ex. 00:00), 1: 차량번호, 2: 내역(입/출차)
    
    # 출차내역 없을 시 23:59 출차
    
    # 초과한 시간이 단위 시간으로 나누어 떨어지지 않으면 올림
    # math.ceil
    
    def trans(string):
        return int(string[:2]) * 60 + int(string[3:])
    
    
    from collections import defaultdict
    import math
    
    # 차량 번호 별 금액 9999
    use_time = [0] * 10000
    
    # 차가 주차장 사용 중 인가
    parking = defaultdict(int)
    
    for r in records:
        time, car_number, detail = r.split(' ')
        time = trans(time)
        
        # 입차
        if detail == 'IN':
            parking[car_number] = time
        
        # 출차
        else:
            start = parking[car_number]
            use = time - start
            
            # 시간 누적
            use_time[int(car_number)] += use
            del parking[car_number]
        
                
    for car_num, start in parking.items():
        use = 23*60 + 59 - start
        use_time[int(car_num)] += use
        
    # 차량 번호가 작은 순으로 주차 요금 배열 리턴
    answer = []
    for t in use_time:
        cost = fees[1]
        
        # 시간을 돈으로 바꿔
        if t:
            if t > fees[0]:
                additional_time = t - fees[0]
                time = math.ceil(additional_time / fees[2])
                cost += time * fees[3]
        
            answer.append(cost)
    return answer