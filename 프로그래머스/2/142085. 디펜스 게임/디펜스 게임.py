import heapq
def solution(n, k, enemy):
    enemies = []
    
    for i, e in enumerate(enemy, start = 1):
        # 병사 제거
        n -= e
        heapq.heappush(enemies, -e)
        
        # 병사가 없다
        if n < 0:
            # 무적권 O
            if k:
                k -= 1
                n -= heapq.heappop(enemies)
            
            # 무적권 X
            else:
                return i - 1
         
    return len(enemy)