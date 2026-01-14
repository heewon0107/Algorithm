def solution(n, build_frame):
    frame = set()
    
    # 설치 함수
    def can_build(x, y, command):
        # 기둥 설치
        if command == 0:
            # 1. 바닥
            if y == 0:
                return True
            
            # 2. 기둥 위, 보 위
            for nx, ny, c in [(x, y-1, 0), (x-1, y, 1), (x, y, 1)]:
                if (nx, ny, c) in frame:
                    return True
                
        # 보 설치
        elif command == 1:
            # 1. 기둥 있어야함
            for nx, ny, c in [(x, y-1, 0), (x+1, y-1, 0)]:
                if (nx, ny, c) in frame:
                    return True
            # 2 양 쪽에 보
            if (x-1, y, 1) in frame and (x+1, y, 1) in frame:
                return True
                
        return False
    
    # 제거 함수
    def remove(x, y, command):
        cur = (x, y, command)
        frame.remove(cur)
        # 기둥 제거
        if command == 0:
            # 윗 기둥, 양쪽 보
            for nx, ny, c in [(x, y+1, 0), (x-1, y+1, 1), (x, y+1, 1)]:
                if (nx, ny, c) in frame and not can_build(nx, ny, c):
                    frame.add(cur)
                    return False
        # 보 제거
        elif command == 1:
            # 양쪽 기둥과 보
            for nx, ny, c in [(x, y, 0), (x+1, y, 0), (x-1, y, 1), (x+1, y, 1)]:
                if (nx, ny, c) in frame and not can_build(nx, ny, c):
                    frame.add(cur)
                    return False
                
        return True
    
    # Maximum O(1000*4)
    for x, y, kind, command in build_frame:
        # 설치
        if command == 1 and can_build(x, y, kind):
            frame.add((x, y, kind))
        # 제거
        elif command == 0:
            remove(x, y, kind)
            
    answer = list(frame)
    answer.sort()
    return answer