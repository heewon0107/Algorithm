def solution(record):
    answer = []
    db = {}
    # DB 기록 O(100000)
    for r in record:
        log = r.split()
        if log[0] == 'Leave':
            continue
        else:
            db[log[1]] = log[2] # 닉네임 갱신
    
    act = {
        'Enter': '들어왔습니다.',
        'Leave': '나갔습니다.'
    }
    # log 생성 O(100000)
    for r in record:
        log = r.split()
        if log[0] == 'Change':
            continue
        command = f'{db[log[1]]}님이 {act[log[0]]}'
        answer.append(command)
    return answer