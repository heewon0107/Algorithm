import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    k = heapq.heappop(scoville)
    
    # 최소 스코빌 지수가 작으면 섞기
    while k < K and scoville:
        # 두 번째 음식
        second_k = heapq.heappop(scoville)
        heapq.heappush(scoville, k + 2*second_k)
        k = heapq.heappop(scoville)
        answer += 1
        
    if k < K:
        return -1
        
    return answer