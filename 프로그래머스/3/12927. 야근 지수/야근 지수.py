import heapq

def solution(n, works):
    works = [-w for w in works] # 처음 오름차순 정렬
    heapq.heapify(works)
    
    for _ in range(n):
        max_val = -heapq.heappop(works)
        if max_val == 0:
            break
        max_val -= 1
        heapq.heappush(works, -max_val)
    
    return sum(w * w for w in works)
