def solution(places):
    answer = []
    delta = [
                [(-1, 0), (1, 0), (0, -1), (0, 1)],  # 거리 1 상하좌우
                [(-1, -1), (-1, 1), (1, 1), (1, -1)], # 11시 부터 시계 방향
                [(-2, 0), (2, 0), (0, -2), (0, 2)]  # 거리 2 상하좌우
                ]
    
    # 유효성 검사
    def is_valid(r, c):
        return 0 <= r < 5 and 0 <= c < 5
    
    # 거리두기 검사
    def check(r, c, command, place):
        de = delta[command]
        for d in range(4):
            dr, dc = de[d]
            nr = r + dr
            nc = c + dc
            
            # 사람 만났을 때 파티션이 없다.
            if is_valid(nr, nc) and place[nr][nc] == 'P':
                # 거리 1 직선
                if command == 0:
                    return False
                # 거리 2 대각
                elif command == 1 and not (place[nr][c] == 'X' and place[r][nc] == 'X'):
                    return False
                # 거리 2 직선
                elif command == 2 and place[r + dr//2][c + dc//2] != 'X':
                    return False
        return True
    
    # 대기실 순회
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
                    
        can_ = True
        for r, c in people:
            for i in range(3):
                if not check(r, c, i, place):
                    can_ = False
                    break
            if not can_:
                break
        if can_:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer